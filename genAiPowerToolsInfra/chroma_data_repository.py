import chromadb

class ChromaDataRepository:
    def __init__(self):
        #self.client = chromadb.Client()      
        self.client = chromadb.PersistentClient(path="./chroma_db")  # Use persistent client for local storage

    def create_collection(self, name: str):
        return self.client.get_or_create_collection(name)

    def add_document(self, collection, document_id, text_content, meta_data):
        # ensure all parameters are provided
        if not all([collection, document_id, text_content, meta_data]):
            raise ValueError("All parameters must be provided")
        

        #print(f"Adding document with ID: {document_id} to collection: {collection.name}")
        #print(f"Document content: {text_content}")
        #print(f"Document metadata: {meta_data}")

        collection.upsert(
            ids=[document_id],
            documents=[
                text_content
            ],
            metadatas=[meta_data]
        )

    def get_collection(self, name: str):
        return self.client.get_collection(name)

    def get_similar_documents(self, collection, query_string, max_results=10):
        return collection.query(
            query_texts=[query_string],
            n_results=max_results
        )
