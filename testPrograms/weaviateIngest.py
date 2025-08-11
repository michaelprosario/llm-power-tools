import sys
import os
from dotenv import load_dotenv
load_dotenv()

from httpx import Auth
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure
import requests, json
import time
from typing import Dict, Any, List

def validate_environment() -> tuple[str, str]:
    """Validate required environment variables."""
    weaviate_url = os.environ.get("WEAVIATE_URL")
    weaviate_api_key = os.environ.get("WEAVIATE_API_KEY")
    
    if not weaviate_url:
        raise ValueError("WEAVIATE_URL environment variable is required")
    if not weaviate_api_key:
        raise ValueError("WEAVIATE_API_KEY environment variable is required")
    
    print(f"Connecting to: {weaviate_url}")
    print(f"API key present: {'Yes' if weaviate_api_key else 'No'}")
    
    return weaviate_url, weaviate_api_key

def validate_data_object(data_obj: Dict[str, Any], index: int) -> Dict[str, str]:
    """Validate and clean a single data object."""
    errors = []
    
    # Check if data_obj is a dictionary
    if not isinstance(data_obj, dict):
        raise ValueError(f"Object {index}: Expected dictionary, got {type(data_obj)}")
    
    # Check required fields
    required_fields = ["Answer", "Question", "Category"]
    for field in required_fields:
        if field not in data_obj:
            errors.append(f"Missing required field: {field}")
        elif data_obj[field] is None:
            errors.append(f"Field {field} cannot be None")
        elif not isinstance(data_obj[field], str):
            errors.append(f"Field {field} must be a string, got {type(data_obj[field])}")
        elif not str(data_obj[field]).strip():
            errors.append(f"Field {field} cannot be empty")
    
    if errors:
        raise ValueError(f"Object {index + 1}: " + "; ".join(errors))
    
    # Clean and return the object
    return {
        "answer": str(data_obj["Answer"]).strip(),
        "question": str(data_obj["Question"]).strip(),
        "category": str(data_obj["Category"]).strip(),
    }

def create_fallback_collection(client, collection_name: str = "QuestionFallback"):
    """Create a fallback collection without vectorization if the main collection fails."""
    try:
        # Delete existing collection if it exists
        if client.collections.exists(collection_name):
            print(f"Deleting existing fallback collection '{collection_name}'...")
            client.collections.delete(collection_name)
        
        # Create new collection without vectorization
        print(f"Creating fallback collection '{collection_name}' without vectorization...")
        collection = client.collections.create(
            name=collection_name,
            properties=[
                weaviate.classes.config.Property(
                    name="answer", 
                    data_type=weaviate.classes.config.DataType.TEXT
                ),
                weaviate.classes.config.Property(
                    name="question", 
                    data_type=weaviate.classes.config.DataType.TEXT
                ),
                weaviate.classes.config.Property(
                    name="category", 
                    data_type=weaviate.classes.config.DataType.TEXT
                ),
            ],
            # No vectorizer configuration - this will disable vectorization
        )
        print(f"✓ Fallback collection '{collection_name}' created successfully")
        return collection_name
        
    except Exception as e:
        print(f"✗ Failed to create fallback collection: {e}")
        raise

def test_collection_insert(client, collection_name: str) -> bool:
    """Test inserting a simple object to verify the collection works."""
    try:
        questions = client.collections.get(collection_name)
        test_object = {
            "answer": "Test Answer",
            "question": "Test Question", 
            "category": "TEST"
        }
        
        print(f"Testing object insertion in '{collection_name}'...")
        result = questions.data.insert(test_object)
        print(f"✓ Test insert successful in '{collection_name}': {result}")
        
        # Clean up test object
        try:
            questions.data.delete_by_id(result)
            print("✓ Test object cleaned up")
        except Exception as e:
            print(f"Note: Could not clean up test object: {e}")
        
        return True
        
    except Exception as e:
        print(f"✗ Test insert failed in '{collection_name}': {e}")
        return False

def insert_single_object(questions_collection, obj: Dict[str, str], index: int, max_retries: int = 3) -> bool:
    """Insert a single object with retry logic."""
    for attempt in range(max_retries):
        try:
            result = questions_collection.data.insert(obj)
            print(f"✓ Successfully inserted object {index + 1}: {obj['category']} - {obj['question'][:50]}...")
            return True
            
        except Exception as e:
            error_msg = str(e)
            print(f"✗ Attempt {attempt + 1}/{max_retries} failed for object {index + 1}: {error_msg}")
            
            # If it's a vectorization error, we might want to fail fast
            if "vectorize" in error_msg.lower() or ("vector" in error_msg.lower() and "unmarshal" in error_msg.lower()):
                print(f"✗ Vectorization error detected - collection may have configuration issues")
                return False
                
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
            else:
                print(f"✗ Failed to insert object {index + 1} after {max_retries} attempts")
                return False

def main():
    try:
        # Validate environment
        weaviate_url, weaviate_api_key = validate_environment()
        
        # Connect to Weaviate Cloud
        print("Connecting to Weaviate...")
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            auth_credentials=Auth.api_key(weaviate_api_key),
        )
        
        # Test connection
        if not client.is_ready():
            raise ConnectionError("Weaviate client is not ready")
        print("✓ Connected to Weaviate successfully")
        
        # Try to use the main collection first
        collection_name = "Question"
        use_fallback = False
        
        # Check if main collection exists and test it
        if client.collections.exists(collection_name):
            print(f"✓ Collection '{collection_name}' exists")
            if not test_collection_insert(client, collection_name):
                print(f"✗ Main collection '{collection_name}' has issues, creating fallback...")
                collection_name = create_fallback_collection(client)
                use_fallback = True
        else:
            print(f"✗ Collection '{collection_name}' does not exist!")
            print("Creating fallback collection...")
            collection_name = create_fallback_collection(client)
            use_fallback = True
        
        # Get collection
        questions = client.collections.get(collection_name)
        
        if use_fallback:
            print(f"⚠️  Using fallback collection '{collection_name}' without vectorization")
        
        # Fetch data
        print("Fetching data from remote source...")
        try:
            resp = requests.get(
                "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json",
                timeout=30
            )
            resp.raise_for_status()  # Raise exception for bad status codes
            data = json.loads(resp.text)
            print(f"✓ Fetched {len(data)} objects from remote source")
        except requests.RequestException as e:
            print(f"✗ Failed to fetch data: {e}")
            return 1
        except json.JSONDecodeError as e:
            print(f"✗ Failed to parse JSON data: {e}")
            return 1
        
        if not data:
            print("✗ No data received")
            return 1
        
        # Validate data structure
        print(f"Sample object structure: {data[0] if data else 'No data'}")
        
        # Process each object individually
        successful_inserts = 0
        failed_inserts = 0
        failed_objects = []
        vectorization_errors = 0
        
        print(f"\nStarting individual object insertion...")
        for index, data_obj in enumerate(data):
            try:
                # Validate and clean the object
                clean_obj = validate_data_object(data_obj, index)
                
                # Insert the object
                if insert_single_object(questions, clean_obj, index):
                    successful_inserts += 1
                else:
                    failed_inserts += 1
                    
                    # Check if this was a vectorization error
                    last_error = "Insert failed after retries"
                    if "vectorize" in str(last_error).lower():
                        vectorization_errors += 1
                    
                    failed_objects.append({
                        "index": index,
                        "object": data_obj,
                        "reason": last_error
                    })
                    
            except ValueError as e:
                print(f"✗ Validation error for object {index + 1}: {e}")
                failed_inserts += 1
                failed_objects.append({
                    "index": index,
                    "object": data_obj,
                    "reason": str(e)
                })
            except Exception as e:
                print(f"✗ Unexpected error for object {index + 1}: {e}")
                failed_inserts += 1
                failed_objects.append({
                    "index": index,
                    "object": data_obj,
                    "reason": f"Unexpected error: {e}"
                })
        
        # Summary
        print(f"\n=== INGESTION SUMMARY ===")
        print(f"Collection used: {collection_name}")
        print(f"Fallback mode: {'Yes' if use_fallback else 'No'}")
        print(f"Total objects processed: {len(data)}")
        print(f"Successful inserts: {successful_inserts}")
        print(f"Failed inserts: {failed_inserts}")
        if vectorization_errors > 0:
            print(f"Vectorization errors: {vectorization_errors}")
        print(f"Success rate: {(successful_inserts / len(data) * 100):.1f}%")
        
        if failed_objects:
            print(f"\n=== FAILED OBJECTS ===")
            for failed in failed_objects[:5]:  # Show first 5 failures
                print(f"Object {failed['index'] + 1}: {failed['reason']}")
            if len(failed_objects) > 5:
                print(f"... and {len(failed_objects) - 5} more failures")
        
        if successful_inserts > 0:
            print(f"\n✓ Successfully ingested {successful_inserts} objects")
            if vectorization_errors > 0:
                print(f"⚠️  Note: {vectorization_errors} vectorization errors occurred. Consider checking your Ollama service.")
            return 0
        else:
            print(f"\n✗ No objects were successfully ingested")
            if vectorization_errors > 0:
                print(f"⚠️  All failures appear to be vectorization-related. Check your Ollama service configuration.")
            return 1
        
    except Exception as e:
        print(f"✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    finally:
        if 'client' in locals():
            client.close()
            print("✓ Weaviate client connection closed")

if __name__ == "__main__":
    sys.exit(main())
