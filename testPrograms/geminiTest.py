# adjust path to include the parent directory
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsCore.prompts.get_summary_prompt import GetSummaryPrompt
from genAiPowerToolsCore.prompts.get_content_tags_prompt import GetContentTagsPrompt
from genAiPowerToolsInfra.gemini_service_provider import GeminiServiceProvider
from genAiPowerToolsInfra.tiktoken_estimator import TikTokenEstimator

# create gemini service provider
model_config = ModelConfig(model_name="gemini-1.5-flash")
model_config.api_key = os.getenv('GEMINI_API_KEY')  # Ensure you set your API key in the environment
if not model_config.api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

gemini_service_provider = GeminiServiceProvider(model_config)

async def summary_example():
    # read data from data2.txt
    text = ""
    with open('data2.txt', 'r') as file:
        text = file.read()

    summary_prompt = GetSummaryPrompt(text).getText()

    command = ExecutePromptCommand(prompt=summary_prompt, context={})
    result = await gemini_service_provider.execute_prompt(command)
    print("Summary:")
    print(result.content)

async def get_content_tags_example():
    # read data from data2.txt
    text = ""
    with open('data2.txt', 'r') as file:
        text = file.read()

    content_tags_prompt = GetContentTagsPrompt(text).getText()

    command = ExecutePromptCommand(prompt=content_tags_prompt, context={})
    result = await gemini_service_provider.execute_prompt(command)
    print("Content Tags:")
    print(result.content)

def tokeSizeEstimator():
    text = ""
    with open('data2.txt', 'r') as file:
        text = file.read()

    estimator = TikTokenEstimator()
    token_count = estimator.estimate_tokens(text)
    print(f"Estimated token count: {token_count}")

async def main():
    await summary_example()
    await get_content_tags_example()
    tokeSizeEstimator()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
