import sys
import os
from dotenv import load_dotenv
from rpds import List
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# get list of developer friendly RSS feeds
# import lib for guids
from genAiPowerToolsInfra.chroma_data_repository import ChromaDataRepository
from genAiPowerToolsInfra.rss_reader_provider import RSSReaderProvider
import chromadb
import uuid

# setup chromadb
repo = ChromaDataRepository()
collection = repo.create_collection("rss_feeds")

while True:
    query = input("Enter a search query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break

    # Get the collection
    collection = repo.get_collection("rss_feeds")

    # Search for similar documents
    results = repo.get_similar_documents(collection, query, 10)

    # Check if we have results
    if not results['ids'][0]:
        print("No results found.")
        continue

    print(f"Number of results found: {len(results['ids'][0])}")
    
    for i in range(len(results['ids'][0])):
        metadata = results['metadatas'][0][i]  # Get the i-th metadata
        document = results['documents'][0][i]   # Get the i-th document
        distance = results['distances'][0][i] if 'distances' in results else None
        
        #print(f"\nResult {i+1}:")
        print(f"Title: {metadata['title']}")
        print(f"Link: {metadata['link']}")

        # check if key exists in metadata
        #if 'summary' in metadata:
        #    print(f"Summary: {metadata['summary']}")
            
        #if distance is not None:
        #    print(f"Similarity Score: {1 - distance:.3f}")
        print("-" * 80)