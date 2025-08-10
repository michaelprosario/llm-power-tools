# adjust path to include the parent directory
import sys
import os



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


# create gemini service provider
model_config = ModelConfig(model_name="gemini-1.5-flash")
model_config.api_key = os.getenv('GEMINI_API_KEY')  # Ensure you set your API key in the environment
if not model_config.api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

def tokeSizeEstimator():
    text = ""
    with open('data2.txt', 'r') as file:
        text = file.read()

    estimator = TikTokenEstimator()
    token_count = estimator.estimate_tokens(text)
    print(f"Estimated token count: {token_count}")

@kernel_function()
def get_temperature(location: str) -> str:
    if location == "orlando":
        return "100"
    elif location == "miami":
        return "110"
    else:
        return "Unknown"

async def main():
    gemini_service_provider = GeminiServiceProvider(model_config)

    ## add plugin for tempature
    gemini_service_provider.getKernel().add_function(
        "get_temperature",
        get_temperature, 
        "get_temperature"
        )

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
