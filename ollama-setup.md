# Ollama Setup Guide

This guide provides step-by-step instructions to set up Ollama from scratch and install the smallest available sentence transformer model for embedding generation.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
3. [Installing Sentence Transformer Models](#installing-sentence-transformer-models)
4. [Verification and Testing](#verification-and-testing)
5. [Docker Setup (Alternative)](#docker-setup-alternative)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

- Linux, macOS, or Windows system
- At least 8GB of RAM (16GB recommended)
- 4GB+ of free disk space
- Internet connection for downloading models
- (Optional) NVIDIA GPU with CUDA support for better performance

## Installation Methods

### Method 1: Direct Installation (Recommended)

#### On Linux/macOS:
```bash
# Download and install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
```

#### On Windows:
1. Download the Ollama installer from [https://ollama.ai/download](https://ollama.ai/download)
2. Run the downloaded `.exe` file
3. Follow the installation wizard

#### Manual Installation:
```bash
# Download the binary directly
curl -L https://ollama.ai/download/ollama-linux-amd64 -o ollama
chmod +x ollama
sudo mv ollama /usr/local/bin/
```

### Method 2: Package Managers

#### Using Homebrew (macOS):
```bash
brew install ollama
```

#### Using APT (Ubuntu/Debian):
```bash
# Add Ollama repository
curl -fsSL https://ollama.ai/install.sh | sh
```

## Starting Ollama Service

### Start the service:
```bash
# Start Ollama service
ollama serve
```

The service will start on `http://localhost:11434` by default.

### Verify installation:
```bash
# Check if Ollama is running
curl http://localhost:11434/api/version
```

Expected response:
```json
{"version":"0.1.x"}
```

## Installing Sentence Transformer Models

Ollama supports several embedding models. Here are the smallest and most efficient options:

### Option 1: nomic-embed-text (Smallest - Recommended)
```bash
# Install the smallest sentence transformer model
ollama pull nomic-embed-text
```

**Model Details:**
- Size: ~274MB
- Dimensions: 768
- Context Length: 8192 tokens
- Best for: General-purpose text embeddings

### Option 2: all-minilm (Alternative Small Model)
```bash
# Alternative small embedding model
ollama pull all-minilm
```

**Model Details:**
- Size: ~46MB
- Dimensions: 384
- Context Length: 256 tokens
- Best for: Very lightweight embeddings

### Option 3: mxbai-embed-large (Larger but High Quality)
```bash
# Larger but higher quality model
ollama pull mxbai-embed-large
```

**Model Details:**
- Size: ~669MB
- Dimensions: 1024
- Context Length: 512 tokens
- Best for: High-quality embeddings when size is not a constraint

## Verification and Testing

### 1. List installed models:
```bash
ollama list
```

### 2. Test embedding generation:
```bash
# Test with nomic-embed-text
curl http://localhost:11434/api/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nomic-embed-text",
    "prompt": "Hello, this is a test sentence for embedding generation."
  }'
```

### 3. Python test script:
```python
import requests
import json

def test_embeddings():
    url = "http://localhost:11434/api/embeddings"
    payload = {
        "model": "nomic-embed-text",
        "prompt": "This is a test sentence for embeddings."
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Embedding dimensions: {len(result['embedding'])}")
        print("✅ Embeddings working correctly!")
        return result['embedding']
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    test_embeddings()
```

## Docker Setup (Alternative)

If you prefer using Docker, use the provided docker-compose configuration:

### 1. Navigate to Docker compose directory:
```bash
cd docker_compose/ollama
```

### 2. Start Ollama with Docker:
```bash
# Start the services
docker-compose up -d

# Check if containers are running
docker-compose ps
```

### 3. Install models in Docker container:
```bash
# Execute commands inside the container
docker exec -it ollama ollama pull nomic-embed-text
```

### 4. Access Web UI:
Open `http://localhost:3000` in your browser for the Ollama Web UI.

## Model Comparison

| Model | Size | Dimensions | Context Length | Use Case |
|-------|------|------------|----------------|----------|
| all-minilm | ~46MB | 384 | 256 | Ultra-lightweight |
| nomic-embed-text | ~274MB | 768 | 8192 | **Recommended balance** |
| mxbai-embed-large | ~669MB | 1024 | 512 | High quality |

## Troubleshooting

### Common Issues:

#### 1. Service not starting:
```bash
# Check if port 11434 is in use
sudo lsof -i :11434

# Kill existing process if needed
sudo pkill ollama

# Restart service
ollama serve
```

#### 2. Model download fails:
```bash
# Check disk space
df -h

# Clear Ollama cache
rm -rf ~/.ollama/models/*

# Retry download
ollama pull nomic-embed-text
```

#### 3. Permission errors:
```bash
# Fix permissions
sudo chown -R $USER:$USER ~/.ollama
```

#### 4. GPU not detected (NVIDIA):
```bash
# Check NVIDIA drivers
nvidia-smi

# Install NVIDIA Container Toolkit for Docker
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

### Performance Optimization:

#### 1. Set environment variables:
```bash
# Increase concurrent requests
export OLLAMA_NUM_PARALLEL=4

# Set memory limit
export OLLAMA_MAX_LOADED_MODELS=2
```

#### 2. For Docker deployment:
```yaml
# Add to docker-compose.yaml
environment:
  - OLLAMA_NUM_PARALLEL=4
  - OLLAMA_MAX_LOADED_MODELS=2
```

## API Usage Examples

### Generate Embeddings:
```bash
curl http://localhost:11434/api/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nomic-embed-text",
    "prompt": "Your text here"
  }'
```

### Batch Embeddings:
```python
import requests

def get_embeddings_batch(texts, model="nomic-embed-text"):
    embeddings = []
    for text in texts:
        response = requests.post(
            "http://localhost:11434/api/embeddings",
            json={"model": model, "prompt": text}
        )
        if response.status_code == 200:
            embeddings.append(response.json()["embedding"])
    return embeddings

# Usage
texts = ["First sentence", "Second sentence", "Third sentence"]
embeddings = get_embeddings_batch(texts)
```

## Next Steps

After successful installation:

1. **Integrate with your application**: Use the API endpoints to generate embeddings
2. **Scale up**: Consider GPU acceleration for production workloads
3. **Monitor performance**: Set up logging and monitoring for production use
4. **Security**: Configure authentication and network security for production deployments

For more advanced configurations and model options, visit the [official Ollama documentation](https://github.com/ollama/ollama).
