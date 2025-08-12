from typing import List

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