# adjust path to include the parent directory
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsCore.prompts.get_summary_prompt import GetSummaryPrompt
from genAiPowerToolsCore.prompts.get_entity_extractor_prompt import GetEntityExtractor
from genAiPowerToolsCore.prompts.get_content_tags_prompt import GetContentTagsPrompt
from genAiPowerToolsInfra.gemini_service_provider import GeminiServiceProvider
from genAiPowerToolsInfra.tiktoken_estimator import TikTokenEstimator

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.functions import kernel_function
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig
from semantic_kernel.functions import kernel_function
from genAiPowerToolsInfra.exa_search_provider import ExaSearchProvider



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

async def main():
    gemini_service_provider = GeminiServiceProvider(model_config)

    # Add plugin for temperature - fix the function registration
    kernel = gemini_service_provider.getKernel()

    weatherPlugin = WeatherPlugin()
    kernel.add_plugin(weatherPlugin, "Weather")
    webSearchPlugin = WebSearchPlugin()
    kernel.add_plugin(webSearchPlugin, "WebSearch")

    # read data from data2.txt
    while True:
        text = ""
        userInput = input("Enter your query: ")

        command = ExecutePromptCommand(prompt=userInput, context={})
        result = await gemini_service_provider.execute_prompt(command)

        print(f"Response: {result.content}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
