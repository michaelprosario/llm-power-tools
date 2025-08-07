## Tutorial can be found at https://docs.weaviate.io/weaviate/quickstart/local

import weaviate
from weaviate.classes.config import Configure
import requests, json

# Connect to Weaviate running on Windows host from WSL
# Use host.docker.internal or the actual Windows IP address
client = weaviate.connect_to_local(
    host="172.30.176.1",
    port=8080,
    grpc_port=50051,
)

questions = client.collections.create(
    name="Question",
    vector_config=Configure.Vectors.text2vec_ollama(  # Configure the Ollama embedding integration
        api_endpoint="http://ollama:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="nomic-embed-text",  # The model to use
    ),
    generative_config=Configure.Generative.ollama(  # Configure the Ollama generative integration
        api_endpoint="http://ollama:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="llama3.2",  # The model to use
    ),
)

client.close()  # Free up resources