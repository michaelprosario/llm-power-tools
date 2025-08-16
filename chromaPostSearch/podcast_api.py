from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import sys
import os

# Add the parent directory to the Python path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from genAiPowerToolsInfra.chroma_data_repository import ChromaDataRepository
from chromaPostSearch.podcastPost import PodcastPost

app = FastAPI(
    title="Podcast Search API",
    description="API for searching and managing podcasts using ChromaDB",
    version="1.0.0"
)

# Initialize ChromaDB repository
chroma_repo = ChromaDataRepository()
COLLECTION_NAME = "podcasts"

# Pydantic models for API requests and responses
class PodcastRequest(BaseModel):
    id: str = Field(..., description="Unique identifier for the podcast")
    content_source_id: str = Field(..., description="Source identifier for the content")
    title: str = Field(..., description="Title of the podcast episode")
    source_url: str = Field(..., description="URL to the podcast source")
    description: str = Field(..., description="Description of the podcast episode")
    enclosure_url: str = Field(..., description="Direct URL to the podcast audio file")

class PodcastResponse(BaseModel):
    id: str
    content_source_id: str
    title: str
    source_url: str
    description: str
    enclosure_url: str

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Search query for finding similar podcasts")
    max_results: int = Field(default=10, ge=1, le=100, description="Maximum number of results to return")

class SearchResponse(BaseModel):
    results: List[PodcastResponse]
    total_results: int

class StatusResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ErrorResponse(BaseModel):
    status: str
    message: str

@app.on_event("startup")
async def startup_event():
    """Initialize the ChromaDB collection on startup"""
    try:
        chroma_repo.create_collection(COLLECTION_NAME)
    except Exception as e:
        print(f"Error initializing collection: {e}")

@app.get("/", response_model=dict)
async def root():
    """Root endpoint providing API information"""
    return {
        "message": "Podcast Search API",
        "version": "1.0.0",
        "endpoints": {
            "search": "/search - POST - Search for similar podcasts",
            "add": "/podcasts - POST - Add a new podcast to the repository",
            "health": "/health - GET - Check API health"
        }
    }

@app.get("/health", response_model=StatusResponse)
async def health_check():
    """Health check endpoint"""
    try:
        # Try to get the collection to verify ChromaDB is accessible
        collection = chroma_repo.get_collection(COLLECTION_NAME)
        return StatusResponse(status="ok", message="API is healthy and ChromaDB is accessible")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "error", "message": f"ChromaDB is not accessible: {str(e)}"}
        )

@app.post("/search", response_model=SearchResponse)
async def get_similar_documents(search_request: SearchRequest):
    """
    Search for podcasts similar to the provided query
    
    Args:
        search_request: Contains the search query and maximum results
        
    Returns:
        SearchResponse with matching podcast results
        
    Raises:
        HTTPException: If query is empty or there's an error accessing the database
    """
    try:
        # Validate query is not empty (Pydantic already handles this, but being explicit)
        if not search_request.query.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"status": "validation error", "message": "Query cannot be empty"}
            )
        
        # Get the collection
        collection = chroma_repo.get_collection(COLLECTION_NAME)
        
        # Search for similar documents
        results = chroma_repo.get_similar_documents(
            collection, 
            search_request.query, 
            search_request.max_results
        )
        
        # Transform results to response format
        podcast_results = []
        if results and results.get('metadatas') and results.get('metadatas')[0]:
            metadatas = results['metadatas'][0]
            ids = results['ids'][0] if results.get('ids') else []
            
            for i, metadata in enumerate(metadatas):
                podcast_id = ids[i] if i < len(ids) else metadata.get('Id', '')
                podcast_results.append(PodcastResponse(
                    id=podcast_id,
                    content_source_id=metadata.get('ContentSourceId', ''),
                    title=metadata.get('Title', ''),
                    source_url=metadata.get('SourceUrl', ''),
                    description=metadata.get('Description', ''),
                    enclosure_url=metadata.get('EnclosureUrl', '')
                ))
        
        return SearchResponse(
            results=podcast_results,
            total_results=len(podcast_results)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": f"An error occurred while searching: {str(e)}"}
        )

@app.post("/podcasts", response_model=StatusResponse)
async def add_podcast(podcast: PodcastRequest):
    """
    Add a new podcast to the ChromaDB repository
    
    Args:
        podcast: Podcast data to be added
        
    Returns:
        StatusResponse indicating success or failure
        
    Raises:
        HTTPException: If validation fails or there's an error adding to the database
    """
    try:
        # Create PodcastPost object from the request
        podcast_post = PodcastPost(
            id=podcast.id,
            content_source_id=podcast.content_source_id,
            title=podcast.title,
            source_url=podcast.source_url,
            description=podcast.description,
            enclosure_url=podcast.enclosure_url
        )
        
        # Get the collection
        collection = chroma_repo.get_collection(COLLECTION_NAME)
        
        # Prepare metadata
        metadata = {
            'Id': podcast_post.id,
            'ContentSourceId': podcast_post.content_source_id,
            'Title': podcast_post.title,
            'SourceUrl': podcast_post.source_url,
            'Description': podcast_post.description,
            'EnclosureUrl': podcast_post.enclosure_url
        }
        
        # Add document to ChromaDB
        # Using the description as the text content for similarity search
        chroma_repo.add_document(
            collection=collection,
            document_id=podcast_post.id,
            text_content=f"{podcast_post.title} {podcast_post.get_clean_description()}",
            meta_data=metadata
        )
        
        return StatusResponse(status="ok", message="Podcast added successfully")
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"status": "validation error", "message": str(e)}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": f"An error occurred while adding the podcast: {str(e)}"}
        )

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return exc.detail

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
