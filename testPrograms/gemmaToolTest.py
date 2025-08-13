import sys
import os
from dotenv import load_dotenv
from rpds import List
from sentence_transformers import SentenceTransformer
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from weaviateInfra.weaviate_search_service import WeaviateSearchService
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsInfra.ollama_service_provider import OllamaServiceProvider
from semantic_kernel.functions import kernel_function
from weaviate.classes.init import Auth
import weaviate

## create plugin to search podcasts by a query string
class PodcastSearchPlugin:
    def __init__(self, search_service: WeaviateSearchService):
        self.search_service = search_service

    @kernel_function(
        name = "podcast_search",
        description="Search for podcasts by a query"
    )

    def search(self, query: str):
        print(f">>>> Searching podcasts for {query} ")
    
        results = self.search_service.get_similar_content("Podcasts", query)

        podcast_list = ""

        for i, obj in enumerate(results.objects, 1):
            properties = obj.properties
            score = obj.metadata.score if obj.metadata else "N/A"
        
            title = properties.get('title', 'N/A')
            description = properties.get('description', 'N/A')
            source = properties.get('sourceUrl', 'N/A')
            podcast_id = properties.get('podcastId', 'N/A')            
            
            podcast_list += f"\nTitle: {title}"
            podcast_list += f"\nDescription: {description[:200]}..."
            podcast_list += f"\nSource Link: {source}"
            podcast_list += f"\nPodcast ID: {podcast_id}"            
            podcast_list += "\n" + "-" * 80

            print(podcast_list)
            
        return podcast_list    





async def main():
    # create service provider
    model_config = ModelConfig("gemma3:1b")
    model_config.base_url = "http://localhost:11434"
    model_config.system_prompt = """
        You are a helpful AI assistant with access to useful tools:
        - podcast_search.search: Search for podcasts by a query

        Use these tools when appropriate to help users.

    """

    ollama_service_provider = OllamaServiceProvider(model_config)
    kernel = ollama_service_provider.getKernel()

    weaviate_url = os.environ["WEAVIATE_URL"]
    weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

    # Setup podcast search with Weaviate vector search
    embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    print("Embedding Model loaded successfully!")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key),
    )

    podcastSearchService = WeaviateSearchService(
        client=client,
        embeddingModel=embedding_model
    )

    ## ollama._types.ResponseError: registry.ollama.ai/library/gemma3:1b does not support tools (status code: 400)
    ## sadness :(
    podcastSearchPlugin = PodcastSearchPlugin(podcastSearchService)
    kernel.add_plugin(podcastSearchPlugin, "PodcastSearch")

    while True:
        userInput = input("Enter your query: ")
        if userInput.lower() == 'exit':
            break

        command = ExecutePromptCommand(prompt=userInput, context={})
        result = await ollama_service_provider.execute_prompt(command)
        print(f"Response: {result.content}\n")

    podcastSearchService.client.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
