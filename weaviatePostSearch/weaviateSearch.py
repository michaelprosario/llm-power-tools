import sys
import os
from dotenv import load_dotenv
load_dotenv()

from httpx import Auth
from sentence_transformers import SentenceTransformer
from typing import List
from weaviate.classes.init import Auth
import weaviate

# Load environment variables
weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

class WeaviateSearchService:

    def __init__(self, client, embeddingModel):
        self.client = client
        self.embeddingModel = embeddingModel

    def get_similar_content(self, collection_name: str, query_text: str) -> List[dict]:
        
        if collection_name is None or query_text is None:
            raise ValueError("Collection name and query text must be provided")

        query_vector = self.create_query_embedding(query_text)
        response = self.get_similar_content_by_vector(collection_name, query_vector)
        return response

    def get_similar_content_by_vector(self, collection_name, query_vector):
        
        if not collection_name or not query_vector:
            raise ValueError("Collection name and query vector must be provided")

        content_collection = self.client.collections.get(collection_name)

        response = content_collection.query.near_vector(
            near_vector=query_vector,
            limit=5,
            return_metadata=['score']
        )

        return response

    def create_query_embedding(self, query_text: str) -> List[float]:
        
        if not query_text:
            raise ValueError("Query text is empty")

        embedding = self.embeddingModel.encode(query_text)
        return embedding.tolist()    


collection_name = "Podcasts"

embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
print("Embedding Model loaded successfully!")


# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
)

podcastSearchService = WeaviateSearchService(client, embedding_model)

while True:

    query_text = input("Enter your search query (or 'exit' to quit): ")
    if query_text.lower() == 'exit':
        break

    response = podcastSearchService.get_similar_content(collection_name, query_text)

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