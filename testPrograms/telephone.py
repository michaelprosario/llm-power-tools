# adjust path to include the parent directory
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# create gemini service provider
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from genAiPowerToolsInfra.ollama_service_provider import OllamaServiceProvider

# create service provider
model_config = ModelConfig("gemma3:4b")
model_config.temperature = 0.8

# connect to local ollama instance ouside of wsl
model_config.base_url = "http://localhost:11434"

ollama_service_provider = OllamaServiceProvider(model_config)

async def main():
    story = """
    Explore a funny story of Luke Skywalker teaching a group of young Jedi and the pranks the students pull on each other
    """
    print(story)
    print("===")

    for i in range(5):
        prompt = f"Continue the story.  Make it funny.  Do not include editorial notes: {story}"

        command = ExecutePromptCommand(prompt)
        result = await ollama_service_provider.execute_prompt(command)
        story = result.content  
        print(story)
        print("===")        

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
