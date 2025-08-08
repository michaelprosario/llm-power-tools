import os
import json
from pathlib import Path
from typing import List, Dict, Any
import weaviate
from weaviate.classes.config import Configure
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WeaviateTextIngester:
    """Class to handle ingestion of text files into Weaviate."""
    
    def __init__(self, weaviate_url: str = "http://localhost:8080"):
        """Initialize connection to Weaviate."""
        self.client = weaviate.connect_to_local(
            host=weaviate_url.replace("http://", "").replace("https://", "")
        )
        logger.info(f"Connected to Weaviate at {weaviate_url}")
    
    def create_schema(self, class_name: str = "Document"):
        """Create schema for storing documents."""
        try:
            # Check if collection already exists
            if self.client.collections.exists(class_name):
                logger.info(f"Collection '{class_name}' already exists")
                return
            
            # Create collection with properties
            collection = self.client.collections.create(
                name=class_name,
                vectorizer_config=Configure.Vectorizer.text2vec_transformers(),
                properties=[
                    weaviate.classes.config.Property(
                        name="content",
                        data_type=weaviate.classes.config.DataType.TEXT,
                        description="The text content of the document"
                    ),
                    weaviate.classes.config.Property(
                        name="filename",
                        data_type=weaviate.classes.config.DataType.TEXT,
                        description="Name of the source file"
                    ),
                    weaviate.classes.config.Property(
                        name="filepath",
                        data_type=weaviate.classes.config.DataType.TEXT,
                        description="Full path to the source file"
                    ),
                    weaviate.classes.config.Property(
                        name="file_size",
                        data_type=weaviate.classes.config.DataType.INT,
                        description="Size of the file in bytes"
                    ),
                    weaviate.classes.config.Property(
                        name="content_length",
                        data_type=weaviate.classes.config.DataType.INT,
                        description="Length of the content in characters"
                    )
                ]
            )
            logger.info(f"Created collection '{class_name}'")
            
        except Exception as e:
            logger.error(f"Error creating schema: {e}")
            raise
    
    def read_text_files(self, folder_path: str) -> List[Dict[str, Any]]:
        """Read all text files from a folder."""
        documents = []
        folder = Path(folder_path)
        
        if not folder.exists():
            logger.error(f"Folder '{folder_path}' does not exist")
            return documents
        
        # Common text file extensions
        text_extensions = {'.txt', '.md', '.rst', '.py', '.js', '.html', '.css', '.json', '.xml', '.csv'}
        
        for file_path in folder.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in text_extensions:
                try:
                    # Read file content
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Skip empty files
                    if not content.strip():
                        logger.warning(f"Skipping empty file: {file_path}")
                        continue
                    
                    # Create document object
                    document = {
                        'content': content,
                        'filename': file_path.name,
                        'filepath': str(file_path.absolute()),
                        'file_size': file_path.stat().st_size,
                        'content_length': len(content)
                    }
                    
                    documents.append(document)
                    logger.info(f"Read file: {file_path} ({len(content)} chars)")
                    
                except Exception as e:
                    logger.error(f"Error reading file {file_path}: {e}")
        
        logger.info(f"Read {len(documents)} documents from '{folder_path}'")
        return documents
    
    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """Split text into overlapping chunks."""
        if len(text) <= chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            
            # Try to end chunk at sentence boundary
            if end < len(text):
                last_period = chunk.rfind('.')
                last_newline = chunk.rfind('\n')
                boundary = max(last_period, last_newline)
                
                if boundary > start + chunk_size // 2:
                    chunk = text[start:start + boundary + 1]
                    end = start + boundary + 1
            
            chunks.append(chunk.strip())
            start = end - overlap
            
            if start >= len(text):
                break
        
        return chunks
    
    def ingest_documents(self, documents: List[Dict[str, Any]], class_name: str = "Document", 
                        chunk_texts: bool = True, chunk_size: int = 1000) -> int:
        """Ingest documents into Weaviate."""
        collection = self.client.collections.get(class_name)
        ingested_count = 0
        
        for doc in documents:
            try:
                if chunk_texts and len(doc['content']) > chunk_size:
                    # Split large documents into chunks
                    chunks = self.chunk_text(doc['content'], chunk_size)
                    
                    for i, chunk in enumerate(chunks):
                        chunk_doc = doc.copy()
                        chunk_doc['content'] = chunk
                        chunk_doc['filename'] = f"{doc['filename']}_chunk_{i+1}"
                        chunk_doc['content_length'] = len(chunk)
                        
                        collection.data.insert(chunk_doc)
                        ingested_count += 1
                        logger.debug(f"Ingested chunk {i+1} of {doc['filename']}")
                else:
                    # Insert document as-is
                    collection.data.insert(doc)
                    ingested_count += 1
                
                logger.info(f"Ingested: {doc['filename']}")
                
            except Exception as e:
                logger.error(f"Error ingesting document {doc['filename']}: {e}")
        
        logger.info(f"Successfully ingested {ingested_count} documents/chunks")
        return ingested_count
    
    def close(self):
        """Close connection to Weaviate."""
        self.client.close()
        logger.info("Closed connection to Weaviate")


def main():
    """Main function to run the ingestion process."""
    
    # Initialize ingester
    ingester = WeaviateTextIngester("http://localhost:8080")
    
    try:
        # Create schema
        ingester.create_schema("Document")

        # Read documents
        documents = ingester.read_text_files("data")
        
        if not documents:
            logger.warning("No documents found to ingest")
            return
        
        # Ingest documents
        count = ingester.ingest_documents(
            documents, 
            "Document",
            chunk_texts=True,
            chunk_size=1000
        )
        
        logger.info(f"Ingestion complete! Processed {count} items.")
        
    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
    finally:
        ingester.close()


if __name__ == "__main__":
    main()