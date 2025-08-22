# LLM Power Tools

A comprehensive suite of AI-powered tools and services for data ingestion, search, and analysis using various LLM providers and vector databases.

## Project Structure Overview

### Core Libraries

#### `genAiPowerToolsCore/`
Core LLM service abstractions and utilities
- **`llm_services.py`** - Main service interfaces for LLM providers
- **`token_estimator.py`** - Token counting and estimation utilities
- **`prompts/`** - Reusable prompt templates

#### `genAiPowerToolsInfra/`
Infrastructure and provider implementations
- **`chroma_data_repository.py`** - ChromaDB vector database integration
- **`exa_search_provider.py`** - Exa search API integration
- **`gemini_service_provider.py`** - Google Gemini LLM service provider
- **`ollama_service_provider.py`** - Ollama local LLM service provider
- **`rss_reader_provider.py`** - RSS feed parsing and ingestion
- **`tiktoken_estimator.py`** - OpenAI tiktoken-based token estimation

### Search and Data Services

#### `chromaPostSearch/`
ChromaDB-based search implementation for podcast data
- **`ingest_data.py`** - Data ingestion pipeline for ChromaDB
- **`podcast_api.py`** - REST API for podcast search
- **`podcastPost.py`** - Podcast-specific data processing
- **`search.py`** - Core search functionality
- **`test_api.py`** - API testing utilities
- **`chroma_db/`** - ChromaDB storage directory

#### `weaviatePostSearch/`
Weaviate vector database integration
- **`import_data.py`** - General data import utilities
- **`import_pod_data_to_weaviate.py`** - Podcast-specific Weaviate ingestion
- **`weaviateSearch.py`** - Weaviate search implementation

#### `weaviateInfra/`
Weaviate infrastructure services
- **`weaviate_search_service.py`** - Core Weaviate search service

### Development and Testing

#### `testPrograms/`
Experimental and testing programs
- **`dev_links_ingest.py`** - RSS feed ingestion with popular dev blogs
- **`geminiTest.py`** - Google Gemini API testing
- **`geminiTestTools.py`** - Gemini function calling tests
- **`gemmaSummaryTest.py`** - Local Gemma model summarization tests
- **`gemmaTest.py`** - General Gemma model testing
- **`rss_reader.py`** - RSS reading utilities
- **`searchTest.py`** - Search functionality testing

#### `genAiPowerToolsUnitTests/`
Unit test suites
- **`llm_services_tests.py`** - Core LLM service testing

### Data and Configuration

#### `data/`
Sample and test data
- **`podcastData/`** - JSON files containing podcast episode data

#### `docker_compose/`
Docker deployment configurations
- **`combined/`** - Multi-service Docker Compose setup
- **`ollama/`** - Ollama-specific deployment
- **`weaviate/`** - Weaviate-specific deployment

#### `docs/`
Documentation and usage guides
- **`ollamaUsage.md`** - Ollama setup and usage instructions

### Application Layer

#### `apps/`
Application-specific implementations and requirements

## Key Features

- **Multi-LLM Support**: Integrations with Google Gemini, Ollama, and other LLM providers
- **Vector Database Integration**: Support for both ChromaDB and Weaviate
- **RSS Feed Processing**: Automated ingestion and processing of developer blogs and news feeds
- **Podcast Search**: Specialized search capabilities for podcast content
- **RESTful APIs**: HTTP APIs for search and data access
- **Docker Support**: Containerized deployment options
- **Token Management**: Intelligent token counting and estimation

## Getting Started

### Virtual Environment Setup

```bash
# Navigate to your project directory
cd /workspaces/llm-power-tools

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Docker Deployment

Choose from the available Docker Compose configurations in `docker_compose/` based on your needs:
- Use `combined/` for a full multi-service setup
- Use `ollama/` for local LLM deployment
- Use `weaviate/` for vector database only

## Notes

- **Gemma Context Window**: The Google Gemma 3B model has a 128K token context window, making it suitable for processing large documents and complex reasoning chains
- **Development Focus**: This project emphasizes developer productivity tools, RSS feed aggregation, and AI-powered search capabilities

