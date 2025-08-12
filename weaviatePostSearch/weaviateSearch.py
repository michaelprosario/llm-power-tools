import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from weaviateInfra.weaviate_search_service import WeaviateSearchService
load_dotenv()

from httpx import Auth
from sentence_transformers import SentenceTransformer
from typing import List
from weaviate.classes.init import Auth
import weaviate

weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]
 
collection_name = "Podcasts"

embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
print("Embedding Model loaded successfully!")

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