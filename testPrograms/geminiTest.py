# adjust path to include the parent directory
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsGemini.gemini_service_provider import GeminiServiceProvider

# create gemini service provider
model_config = ModelConfig(model_name="gemini-1.5-flash")
model_config.api_key = os.getenv('GEMINI_API_KEY')  # Ensure you set your API key in the environment
if not model_config.api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

gemini_service_provider = GeminiServiceProvider(model_config)

async def main():
    command = ExecutePromptCommand(prompt="Write a poem about star trek", context={"theme": "science fiction"})
    result = await gemini_service_provider.execute_prompt(command)
    print(result.content)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
