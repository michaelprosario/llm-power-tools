# ChromaPostSearch Docker Guide

This guide provides instructions for building and running the ChromaPostSearch application using Docker.

## Prerequisites

- Docker installed and running on your system
- Access to the llm-power-tools repository

## Building the Docker Image

### 1. Navigate to the Project Root

```bash
cd /path/to/llm-power-tools
```

### 2. Build the Docker Image

```bash
docker build -t chromapostsearch:latest .
```

This command will:
- Use the Dockerfile in the project root
- Install all required Python dependencies (FastAPI, uvicorn, pydantic, chromadb)
- Copy the application files and ChromaDB database
- Create a container ready to serve the podcast search API

## Running the Container

### 1. Run the Container

```bash
docker run -d -p 8000:8000 --name chromapostsearch chromapostsearch:latest
```

Options explained:
- `-d`: Run in detached mode (background)
- `-p 8000:8000`: Map port 8000 from container to host
- `--name chromapostsearch`: Give the container a friendly name
- `chromapostsearch:latest`: Use the image we built

### 2. Verify the Container is Running

```bash
docker ps
```

You should see the `chromapostsearch` container in the list with status "Up".

## Testing the API

### 1. Health Check

Test if the API is responding:

```bash
curl http://localhost:8000
```

You should receive a JSON response with API information and available endpoints.

### 2. API Documentation

Once the container is running, you can access the interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Available API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and health check |
| `/search` | POST | Search for similar podcasts |
| `/podcasts` | POST | Add a new podcast to the repository |
| `/health` | GET | Health check endpoint |

## Container Management

### Stop the Container

```bash
docker stop chromapostsearch
```

### Start the Container Again

```bash
docker start chromapostsearch
```

### Remove the Container

```bash
docker rm -f chromapostsearch
```

### View Container Logs

```bash
docker logs chromapostsearch
```

### Execute Commands in Running Container

```bash
docker exec -it chromapostsearch /bin/bash
```

## Troubleshooting

### Container Won't Start

1. Check the logs:
   ```bash
   docker logs chromapostsearch
   ```

2. Ensure port 8000 is not already in use:
   ```bash
   netstat -an | grep 8000
   ```

3. Try running with different port mapping:
   ```bash
   docker run -d -p 8001:8000 --name chromapostsearch chromapostsearch:latest
   ```

### Rebuild After Code Changes

1. Stop and remove the existing container:
   ```bash
   docker rm -f chromapostsearch
   ```

2. Rebuild the image:
   ```bash
   docker build -t chromapostsearch:latest .
   ```

3. Run the new container:
   ```bash
   docker run -d -p 8000:8000 --name chromapostsearch chromapostsearch:latest
   ```

## Development Tips

### Mount Local Code for Development

For development purposes, you can mount your local code to see changes without rebuilding:

```bash
docker run -d -p 8000:8000 \
  -v $(pwd)/chromaPostSearch:/app/chromaPostSearch \
  -v $(pwd)/genAiPowerToolsInfra:/app/genAiPowerToolsInfra \
  --name chromapostsearch-dev \
  chromapostsearch:latest
```

### Environment Variables

You can pass environment variables to customize the application:

```bash
docker run -d -p 8000:8000 \
  -e PYTHONPATH=/app \
  --name chromapostsearch \
  chromapostsearch:latest
```

## Docker Compose (Optional)

For easier management, you can create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  chromapostsearch:
    build: .
    ports:
      - "8000:8000"
    container_name: chromapostsearch
    restart: unless-stopped
```

Then use:
```bash
docker-compose up -d    # Start
docker-compose down     # Stop and remove
docker-compose logs     # View logs
```

## Architecture Overview

The Docker container includes:
- **Python 3.12** runtime environment
- **FastAPI** web framework for the REST API
- **Uvicorn** ASGI server for serving the application
- **ChromaDB** vector database for podcast search functionality
- **Pre-loaded podcast database** with existing podcast data

The application serves a REST API that allows you to search through podcast content using vector similarity search powered by ChromaDB.
