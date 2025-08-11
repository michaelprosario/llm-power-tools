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
        auth_config = weaviate.AuthApiKey(api_key=self.weaviate_api_key)
        self.client = weaviate.Client(
            url=self.weaviate_url,
            auth_client_secret=auth_config
        )
        
        # Initialize embedding model
        print("Loading embedding model...")
        self.embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        print("Model loaded successfully!")
        
    def create_schema(self):
        """Create the Podcasts collection schema in Weaviate."""
        schema = {
            "class": "Podcasts",
            "description": "A collection of podcast episodes",
            "vectorizer": "none",  # We'll provide our own vectors
            "properties": [
                {
                    "name": "podcastId",
                    "dataType": ["text"],
                    "description": "The unique ID of the podcast"
                },
                {
                    "name": "contentSourceId",
                    "dataType": ["text"],
                    "description": "The content source ID"
                },
                {
                    "name": "title",
                    "dataType": ["text"],
                    "description": "The title of the podcast episode"
                },
                {
                    "name": "sourceUrl",
                    "dataType": ["text"],
                    "description": "The source URL of the podcast"
                },
                {
                    "name": "description",
                    "dataType": ["text"],
                    "description": "The description of the podcast episode"
                },
                {
                    "name": "enclosureUrl",
                    "dataType": ["text"],
                    "description": "The URL to the podcast audio file"
                }
            ]
        }
        
        # Check if schema already exists
        try:
            existing_schema = self.client.schema.get("Podcasts")
            print("Podcasts collection already exists. Deleting and recreating...")
            self.client.schema.delete_class("Podcasts")
        except Exception as e:
            print("Podcasts collection doesn't exist yet.")
        
        # Create the schema
        self.client.schema.create_class(schema)
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
    
    def load_podcast_files(self, data_dir: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Load the first N podcast JSON files from the directory."""
        podcast_files = glob.glob(os.path.join(data_dir, "podcast_*.json"))
        podcast_files.sort()  # Ensure consistent ordering
        
        podcasts = []
        for i, file_path in enumerate(podcast_files[:limit]):
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
                data_object = {
                    "podcastId": podcast_id,
                    "contentSourceId": content_source_id,
                    "title": title,
                    "sourceUrl": source_url,
                    "description": description,
                    "enclosureUrl": enclosure_url
                }
                
                # Import to Weaviate
                self.client.data_object.create(
                    data_object=data_object,
                    class_name="Podcasts",
                    vector=embedding
                )
                
                print(f"✓ Imported podcast {i+1}: {title[:60]}...")
                
            except Exception as e:
                print(f"✗ Error importing podcast {i+1}: {e}")
    
    def verify_import(self):
        """Verify the import by checking the count of objects in the collection."""
        try:
            result = self.client.query.aggregate("Podcasts").with_meta_count().do()
            count = result['data']['Aggregate']['Podcasts'][0]['meta']['count']
            print(f"\nVerification: {count} podcasts imported successfully!")
            
            # Show a sample object
            sample = self.client.query.get("Podcasts", ["title", "podcastId"]).with_limit(1).do()
            if sample['data']['Get']['Podcasts']:
                sample_title = sample['data']['Get']['Podcasts'][0]['title']
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
    data_dir = "/workspaces/llm-power-tools/weaviatePostSearch/podcastData"
    
    # Check if data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Data directory {data_dir} does not exist!")
        return
    
    try:
        # Create schema
        importer.create_schema()
        
        # Load podcast files (first 10)
        podcasts = importer.load_podcast_files(data_dir, limit=10)
        
        if not podcasts:
            print("No podcast files found!")
            return
        
        # Import podcasts
        importer.import_podcasts(podcasts)
        
        # Verify import
        importer.verify_import()
        
        print("\n=== Import completed successfully! ===")
        
    except Exception as e:
        print(f"Error during import process: {e}")

if __name__ == "__main__":
    main()
