#!/bin/bash

# Build and run the chromaPostSearch FastAPI application

echo "Building chromaPostSearch Docker image..."
docker build -t chromapostsearch:latest .

if [ $? -eq 0 ]; then
    echo "Build successful! Starting the container..."
    docker run -d -p 8000:8000 --name chromapostsearch-container chromapostsearch:latest
    echo "Container started. FastAPI is available at http://localhost:8000"
    echo "API documentation available at http://localhost:8000/docs"
else
    echo "Build failed!"
    exit 1
fi
