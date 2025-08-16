# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p /app/chromaPostSearch/chroma_db
RUN mkdir -p /app/genAiPowerToolsInfra

# Copy the FastAPI application files
COPY podcast_api.py /app/chromaPostSearch/
COPY podcastPost.py /app/chromaPostSearch/
COPY search.py /app/chromaPostSearch/

# Copy the infrastructure dependency
COPY ../genAiPowerToolsInfra/chroma_data_repository.py /app/genAiPowerToolsInfra/

# Download chroma.sqlite3 from the specified URL
RUN curl -o /app/chromaPostSearch/chroma_db/chroma.sqlite3 https://storage.googleapis.com/team-focus-data/chroma.sqlite3

# Create an empty __init__.py file for the package
RUN touch /app/genAiPowerToolsInfra/__init__.py
RUN touch /app/chromaPostSearch/__init__.py

# Set Python path to include the app directory
ENV PYTHONPATH=/app

# Expose port 8000
EXPOSE 8000

# Change to the chromaPostSearch directory to ensure proper working directory
WORKDIR /app/chromaPostSearch

# Command to run the FastAPI application
CMD ["python", "podcast_api.py"]
