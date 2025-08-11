#!/usr/bin/env python3
"""
Import podcast data to Weaviate cloud instance.
This script imports the first 10 JSON files from the podcastData directory.
"""

import os
import json
import glob
from typing import List, Dict, Any
import weaviate
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import re
from weaviate.classes.init import Auth

# Load environment variables
load_dotenv()

class PodcastImporter:
    def __init__(self):
        """Initialize the podcast importer with Weaviate client and embedding model."""
        self.weaviate_url = os.getenv('WEAVIATE_URL')
        self.weaviate_api_key = os.getenv('WEAVIATE_API_KEY')
        
        if not self.weaviate_url or not self.weaviate_api_key:
            raise ValueError("WEAVIATE_URL and WEAVIATE_API_KEY must be set in .env file")
        
        # Initialize Weaviate client
        auth_config = Auth.api_key(self.weaviate_api_key)
        self.client = weaviate.connect_to_weaviate_cloud(
            cluster_url=self.weaviate_url,
            auth_credentials=auth_config
        )
        
        # Initialize embedding model
        print("Loading embedding model...")
        self.embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        print("Model loaded successfully!")

    def close(self):
        """Close the Weaviate client connection."""
        if self.client:
            self.client.close()
            print("Weaviate client connection closed.")

    def create_schema(self):
        """Create the Podcasts collection schema in Weaviate."""
        from weaviate.classes.config import Configure, Property, DataType
        
        # Check if collection already exists
        if self.client.collections.exists("Podcasts"):
            print("Podcasts collection already exists. Deleting and recreating...")
            self.client.collections.delete("Podcasts")
        
        # Create the collection with v4 API
        self.client.collections.create(
            name="Podcasts",
            description="A collection of podcast episodes",
            vectorizer_config=Configure.Vectorizer.none(),  # We'll provide our own vectors
            properties=[
                Property(name="podcastId", data_type=DataType.TEXT, description="The unique ID of the podcast"),
                Property(name="contentSourceId", data_type=DataType.TEXT, description="The content source ID"),
                Property(name="title", data_type=DataType.TEXT, description="The title of the podcast episode"),
                Property(name="sourceUrl", data_type=DataType.TEXT, description="The source URL of the podcast"),
                Property(name="description", data_type=DataType.TEXT, description="The description of the podcast episode"),
                Property(name="enclosureUrl", data_type=DataType.TEXT, description="The URL to the podcast audio file")
            ]
        )
        print("Podcasts collection schema created successfully!")
    
    def clean_html(self, text: str) -> str:
        """Remove HTML tags from text."""
        if not text:
            return ""
        # Remove HTML tags
        clean = re.sub(r'<[^>]+>', '', text)
        # Remove extra whitespace
        clean = re.sub(r'\s+', ' ', clean).strip()
        return clean
    
    def create_embedding(self, title: str, description: str) -> List[float]:
        """Create embedding from title and first 1000 characters of description."""
        # Clean description and take first 1000 characters
        clean_description = self.clean_html(description)[:1000]
        
        # Combine title and description
        text_to_embed = f"{title}. {clean_description}"
        
        # Generate embedding
        embedding = self.embedding_model.encode(text_to_embed)
        return embedding.tolist()
    
    def load_podcast_files(self, data_dir: str) -> List[Dict[str, Any]]:
        """Load the first N podcast JSON files from the directory."""
        podcast_files = glob.glob(os.path.join(data_dir, "podcast_*.json"))
        podcast_files.sort()  # Ensure consistent ordering
        
        podcasts = []
        for i, file_path in enumerate(podcast_files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    podcast_data = json.load(f)
                    podcasts.append(podcast_data)
                    print(f"Loaded podcast {i+1}: {podcast_data.get('Title', 'Unknown')}")
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        return podcasts
    
    def import_podcasts(self, podcasts: List[Dict[str, Any]]):
        """Import podcast data to Weaviate."""
        print(f"\nImporting {len(podcasts)} podcasts to Weaviate...")
        
        # Get the collection
        podcasts_collection = self.client.collections.get("Podcasts")
        
        # Use batch import for better performance
        with podcasts_collection.batch.dynamic() as batch:
            for i, podcast in enumerate(podcasts):
                try:
                    # Extract required fields
                    podcast_id = podcast.get('Id', '')
                    content_source_id = podcast.get('ContentSourceId', '')
                    title = podcast.get('Title', '')
                    source_url = podcast.get('SourceUrl', '')
                    description = podcast.get('Description', '')
                    enclosure_url = podcast.get('EnclosureUrl', '')
                    
                    # Create embedding
                    embedding = self.create_embedding(title, description)
                    
                    # Prepare data object
                    properties = {
                        "podcastId": podcast_id,
                        "contentSourceId": content_source_id,
                        "title": title,
                        "sourceUrl": source_url,
                        "description": description,
                        "enclosureUrl": enclosure_url
                    }
                    
                    # Add to batch with vector
                    batch.add_object(
                        properties=properties,
                        vector=embedding
                    )
                    
                    print(f"✓ Queued podcast {i+1}: {title[:60]}...")
                    
                except Exception as e:
                    print(f"✗ Error processing podcast {i+1}: {e}")
        
        # Check for any failed objects
        failed_objects = podcasts_collection.batch.failed_objects
        if failed_objects:
            print(f"Failed to import {len(failed_objects)} objects")
            for failed in failed_objects[:3]:  # Show first 3 errors
                print(f"Error: {failed.message}")
        else:
            print(f"Successfully imported all {len(podcasts)} podcasts!")
    
    def verify_import(self):
        """Verify the import by checking the count of objects in the collection."""
        try:
            podcasts_collection = self.client.collections.get("Podcasts")
            
            # Get total count using aggregate
            response = podcasts_collection.aggregate.over_all(total_count=True)
            count = response.total_count
            print(f"\nVerification: {count} podcasts imported successfully!")
            
            # Show a sample object
            sample_response = podcasts_collection.query.fetch_objects()
            if sample_response.objects:
                sample_title = sample_response.objects[0].properties.get('title', 'Unknown')
                print(f"Sample imported podcast: {sample_title}")
                
        except Exception as e:
            print(f"Error during verification: {e}")

def main():
    """Main function to run the podcast import process."""
    print("=== Podcast Data Import to Weaviate ===\n")
    
    # Initialize importer
    try:
        importer = PodcastImporter()
    except Exception as e:
        print(f"Error initializing importer: {e}")
        print("\nPlease ensure you have a .env file with:")
        print("WEAVIATE_URL=your_weaviate_cloud_url")
        print("WEAVIATE_API_KEY=your_weaviate_api_key")
        return
    
    # Define data directory
    data_dir = "podcastData"
    
    # Check if data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Data directory {data_dir} does not exist!")
        return
    
    try:
        # Create schema
        importer.create_schema()
        
        # Load podcast files (first 10)
        podcasts = importer.load_podcast_files(data_dir)
        
        if not podcasts:
            print("No podcast files found!")
            return
        
        # Import podcasts
        importer.import_podcasts(podcasts)
        
        # Verify import
        importer.verify_import()
        
        print("\n=== Import completed successfully! ===")
        importer.close()
        
    except Exception as e:
        print(f"Error during import process: {e}")

if __name__ == "__main__":
    main()
