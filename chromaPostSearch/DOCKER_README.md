# ChromaPostSearch Docker Setup

This directory contains Docker configuration for running the ChromaPostSearch FastAPI application.

## Files Created

- `Dockerfile` - Multi-stage Docker build configuration
- `docker-compose.yml` - Docker Compose configuration for easy deployment
- `.dockerignore` - Files to exclude from Docker build context
- `run.sh` - Simple build and run script

## Quick Start

### Option 1: Using the run script
```bash
./run.sh
```

### Option 2: Using Docker directly
```bash
# Build the image
docker build -t chromapostsearch:latest .

# Run the container
docker run -d -p 8000:8000 --name chromapostsearch-container chromapostsearch:latest
```

### Option 3: Using Docker Compose
```bash
# Build and start
docker-compose up -d

# Stop
docker-compose down
```

## Features

- Downloads `chroma.sqlite3` automatically from the specified Google Cloud Storage URL
- Exposes the FastAPI application on port 8000
- Includes health check endpoint
- Persistent volume for ChromaDB data (when using docker-compose)
- Minimal image size using Python slim base image

## API Access

Once running, the API will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- OpenAPI schema: http://localhost:8000/openapi.json

## Container Management

```bash
# View logs
docker logs chromapostsearch-container

# Stop container
docker stop chromapostsearch-container

# Remove container
docker rm chromapostsearch-container

# Remove image
docker rmi chromapostsearch:latest
```

## Environment Variables

The container sets:
- `PYTHONPATH=/app` - Ensures proper module imports
- Working directory: `/app/chromaPostSearch`

## Volume Mounts

When using docker-compose, ChromaDB data is persisted in a named volume `chroma_data`.
