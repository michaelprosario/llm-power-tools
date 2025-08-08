import weaviate
import json

client = weaviate.connect_to_local(
    host="172.30.176.1",
    port=8080,
    grpc_port=50051,
)

questions = client.collections.get("Question")

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