## Tutorial can be found at https://docs.weaviate.io/weaviate/quickstart/local

import sys
import os
from dotenv import load_dotenv
load_dotenv()

import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure
import requests, json

# Connect to Weaviate running on Windows host from WSL
# Use host.docker.internal or the actual Windows IP address
# Best practice: store your credentials in environment variables
weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
)

questions = client.collections.create(
    name="Question",
    vector_config=Configure.Vectors.text2vec_ollama(  # Configure the Ollama embedding integration
        api_endpoint="https://cuddly-robot-4jrx4pgqgwc5xr-11434.app.github.dev",  # If using Docker you might need: http://host.docker.internal:11434
        model="nomic-embed-text",  # The model to use
    ),
    generative_config=Configure.Generative.ollama(  # Configure the Ollama generative integration
        api_endpoint="https://cuddly-robot-4jrx4pgqgwc5xr-11434.app.github.dev",  # If using Docker you might need: http://host.docker.internal:11434
        model="llama3.2",  # The model to use
    ),
)

client.close()  # Free up resources