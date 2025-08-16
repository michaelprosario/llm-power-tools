# Podcast Search API

A FastAPI-based REST API for searching and managing podcasts using ChromaDB for similarity search.

## Features

- **Search Similar Podcasts**: Find podcasts similar to a given query using semantic search
- **Add Podcasts**: Add new podcast episodes to the ChromaDB repository
- **Health Monitoring**: Health check endpoint to verify API and database status
- **Input Validation**: Comprehensive validation for all API inputs
- **Error Handling**: Proper error responses with detailed messages

## API Endpoints

### 1. Root Endpoint
- **URL**: `GET /`
- **Description**: Provides API information and available endpoints
- **Response**: API metadata and endpoint list

### 2. Health Check
- **URL**: `GET /health`
- **Description**: Check if the API and ChromaDB are accessible
- **Response**: 
  ```json
  {
    "status": "ok",
    "message": "API is healthy and ChromaDB is accessible"
  }
  ```

### 3. Search Similar Podcasts
- **URL**: `POST /search`
- **Description**: Search for podcasts similar to the provided query
- **Request Body**:
  ```json
  {
    "query": "machine learning artificial intelligence",
    "max_results": 10
  }
  ```
- **Response**:
  ```json
  {
    "results": [
      {
        "id": "podcast-123",
        "content_source_id": "source-456",
        "title": "AI and Machine Learning Basics",
        "source_url": "https://example.com/podcast",
        "description": "Introduction to AI and ML concepts",
        "enclosure_url": "https://example.com/audio.mp3"
      }
    ],
    "total_results": 1
  }
  ```

### 4. Add Podcast
- **URL**: `POST /podcasts`
- **Description**: Add a new podcast episode to the repository
- **Request Body**:
  ```json
  {
    "id": "unique-podcast-id",
    "content_source_id": "source-identifier",
    "title": "Podcast Episode Title",
    "source_url": "https://example.com/podcast",
    "description": "Detailed description of the podcast episode",
    "enclosure_url": "https://example.com/audio.mp3"
  }
  ```
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "Podcast added successfully"
  }
  ```

## Installation and Setup

### Prerequisites
- Python 3.7+
- ChromaDB
- FastAPI
- Uvicorn

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the API
```bash
python podcast_api.py
```

The API will be available at `http://localhost:8000`

### Interactive Documentation
Once the API is running, you can access:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Testing

Run the test suite to verify all endpoints work correctly:

```bash
python test_api.py
```

Make sure the API is running before executing the tests.

## Error Handling

The API provides comprehensive error handling:

### Validation Errors (400)
- Empty or invalid query parameters
- Missing required fields when adding podcasts
- Invalid data types

### Server Errors (500)
- ChromaDB connection issues
- Internal processing errors

### Service Unavailable (503)
- ChromaDB is not accessible

## Data Model

### Podcast Structure
```python
{
    "id": str,                    # Unique identifier
    "content_source_id": str,     # Source system identifier
    "title": str,                 # Episode title
    "source_url": str,           # URL to podcast page
    "description": str,          # Episode description
    "enclosure_url": str         # Direct audio file URL
}
```

## Usage Examples

### Search for Podcasts
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/json" \
     -d '{
       "query": "python programming",
       "max_results": 5
     }'
```

### Add a New Podcast
```bash
curl -X POST "http://localhost:8000/podcasts" \
     -H "Content-Type: application/json" \
     -d '{
       "id": "py-podcast-001",
       "content_source_id": "python-weekly",
       "title": "Advanced Python Techniques",
       "source_url": "https://pythonweekly.com/episode-001",
       "description": "Deep dive into advanced Python programming techniques and best practices",
       "enclosure_url": "https://pythonweekly.com/episodes/001.mp3"
     }'
```

### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

## ChromaDB Integration

The API uses the existing `ChromaDataRepository` class to interact with ChromaDB:
- **Collection Name**: `podcast_episodes`
- **Storage**: Persistent storage in `./chroma_db` directory
- **Search Method**: Similarity search using embedded vectors
- **Text Content**: Combination of title and description for similarity matching

## Architecture

```
chromaPostSearch/
├── podcast_api.py          # Main FastAPI application
├── podcastPost.py          # Podcast data model
├── test_api.py            # API test suite
├── requirements.txt       # Python dependencies
└── README.md             # This file

genAiPowerToolsInfra/
└── chroma_data_repository.py  # ChromaDB integration
```

## Contributing

1. Follow the existing code style and structure
2. Add tests for new functionality
3. Update this README for new features
4. Ensure all tests pass before submitting changes

## License

This project is part of the llm-power-tools repository.
