import sys
import os
from dotenv import load_dotenv
load_dotenv()

from httpx import Auth
import weaviate
from weaviate.classes.init import Auth
import json

weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
)

questions = client.collections.get("QuestionSimple")

response = questions.query.near_text(
    query="animals",
    limit=5
)


print("Similarity search results (animals)..................")
for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))


print("Rag demo........................")

response = questions.generate.near_text(
    query="biology",
    limit=2,
    grouped_task="Write a tweet with emojis about these facts."
)

print(response.generative.text)  # Inspect the generated text

client.close() 