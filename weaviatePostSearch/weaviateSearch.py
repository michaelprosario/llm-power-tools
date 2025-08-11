import sys
import os
from dotenv import load_dotenv
load_dotenv()

from httpx import Auth
from sentence_transformers import SentenceTransformer
from typing import List
from weaviate.classes.init import Auth
import json
import re
import weaviate

# Load environment variables
weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

# Initialize embedding model (same as import script)
print("Loading embedding model...")
embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
print("Model loaded successfully!")

def create_query_embedding(query_text: str) -> List[float]:
    """Create embedding from query text using the same model as import."""
    # Generate embedding for the query
    embedding = embedding_model.encode(query_text)
    return embedding.tolist()

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
)

# Get the Podcasts collection
podcasts_collection = client.collections.get("Podcasts")


while True:

    query_text = input("Enter your search query (or 'exit' to quit): ")
    query_vector = create_query_embedding(query_text)

    print(f"Searching for: '{query_text}'")
    print("=" * 50)

    # Perform vector similarity search
    response = podcasts_collection.query.near_vector(
        near_vector=query_vector,
        limit=5,
        return_metadata=['score']
    )

    print("Similarity search results ..................")
    for i, obj in enumerate(response.objects, 1):
        properties = obj.properties
        score = obj.metadata.score if obj.metadata else "N/A"
        
        print(f"\n--- Result {i} (Score: {score}) ---")
        print(f"Title: {properties.get('title', 'N/A')}")
        print(f"Description: {properties.get('description', 'N/A')[:200]}...")
        print(f"Source: {properties.get('sourceUrl', 'N/A')}")
        print(f"Podcast ID: {properties.get('podcastId', 'N/A')}")
        print("-" * 80)



client.close() 