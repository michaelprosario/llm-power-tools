# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY chromaPostSearch/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p /app/chromaPostSearch/chroma_db
RUN mkdir -p /app/genAiPowerToolsInfra

# Copy the infrastructure dependency first
COPY genAiPowerToolsInfra/chroma_data_repository.py /app/genAiPowerToolsInfra/

# Copy the FastAPI application files
COPY chromaPostSearch/podcast_api.py /app/chromaPostSearch/
COPY chromaPostSearch/podcastPost.py /app/chromaPostSearch/
COPY chromaPostSearch/search.py /app/chromaPostSearch/

# Copy the existing chroma database
COPY chromaPostSearch/chroma_db/ /app/chromaPostSearch/chroma_db/

# Create __init__.py files for proper Python package structure
RUN touch /app/genAiPowerToolsInfra/__init__.py
RUN touch /app/chromaPostSearch/__init__.py

# Set Python path to include the app directory
ENV PYTHONPATH=/app

# Expose port 8000
EXPOSE 8000

# Change to the chromaPostSearch directory to ensure proper working directory
WORKDIR /app/chromaPostSearch

# Command to run the FastAPI application with uvicorn
CMD ["uvicorn", "podcast_api:app", "--host", "0.0.0.0", "--port", "8000"]
