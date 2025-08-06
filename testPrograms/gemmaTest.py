# adjust path to include the parent directory
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsInfra.ollama_service_provider import OllamaServiceProvider

# create service provider
model_config = ModelConfig("gemma3:4b")

# connect to local ollama instance ouside of wsl
model_config.base_url = "http://localhost:11434"

ollama_service_provider = OllamaServiceProvider(model_config)

async def main():
    command = ExecutePromptCommand(prompt="Write a song about star trek", context={"theme": "science fiction"})
    result = await ollama_service_provider.execute_prompt(command)
    print(result.content)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
