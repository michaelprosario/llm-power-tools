# adjust path to include the parent directory
import sys
import os
from dotenv import load_dotenv
from rpds import List
from sentence_transformers import SentenceTransformer
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsCore.prompts.get_summary_prompt import GetSummaryPrompt
from genAiPowerToolsCore.prompts.get_entity_extractor_prompt import GetEntityExtractor
from genAiPowerToolsCore.prompts.get_content_tags_prompt import GetContentTagsPrompt
from genAiPowerToolsInfra.gemini_service_provider import GeminiServiceProvider
from genAiPowerToolsInfra.tiktoken_estimator import TikTokenEstimator
from weaviateInfra.weaviate_search_service import WeaviateSearchService

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig
from semantic_kernel.functions import kernel_function
from genAiPowerToolsInfra.exa_search_provider import ExaSearchProvider
from weaviate.classes.init import Auth
import weaviate

# create gemini service provider
model_config = ModelConfig(model_name="gemini-1.5-flash")
model_config.api_key = os.getenv('GEMINI_API_KEY')  # Ensure you set your API key in the environment
if not model_config.api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

class WeatherPlugin:
    def __init__(self):
        pass

    @kernel_function(
        name = "get_temperature",
        description="Get current temperature for a place"
    )
    def get_temperature(self, city: str) -> str:
        print(f">>>> Getting temperature for {city} ")
        if "orlando" in city.lower():
            return "Temperature is 100"
        elif "miami" in city.lower():
            return "Temperature is 90"
        else:
            return f"Temperature data for {city} is not available."

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

class WebSearchPlugin:
    def __init__(self):
        self.service = ExaSearchProvider()

    @kernel_function(
        name = "web_search",
        description="Search the web for a query"
    )
    def web_search(self, query: str) -> str:
        print(f">>>> Searching the web for {query} ")
        answerResult = self.service.answer(query=query)
        return answerResult


weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

async def main():
    gemini_service_provider = GeminiServiceProvider(model_config)
    
    kernel = gemini_service_provider.getKernel()

    weatherPlugin = WeatherPlugin()
    kernel.add_plugin(weatherPlugin, "Weather")
    webSearchPlugin = WebSearchPlugin()
    kernel.add_plugin(webSearchPlugin, "WebSearch")        

    
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
    podcastSearchPlugin = PodcastSearchPlugin(podcastSearchService)
    kernel.add_plugin(podcastSearchPlugin, "PodcastSearch")


    # read data from data2.txt
    while True:
        text = ""
        userInput = input("Enter your query: ")
        if userInput.lower() == 'exit':
            break

        command = ExecutePromptCommand(prompt=userInput, context={})
        result = await gemini_service_provider.execute_prompt(command)

        print(f"Response: {result.content}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
