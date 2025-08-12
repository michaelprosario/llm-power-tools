
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig

import asyncio
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.connectors.ai.ollama import OllamaChatPromptExecutionSettings

service_id = "default"

class OllamaServiceProvider(LLMServiceProvider):
    def __init__(self, model_config: ModelConfig):
        super().__init__(model_config)

        model_id = model_config.model_name or "gemma3:4b"  # Default model name if not specified   
        base_url = model_config.base_url or "http://localhost:11434"  # Default base URL if not specified

        self.kernel = Kernel()
        chat_service = OllamaChatCompletion(ai_model_id=model_id)
        self.kernel.add_service(chat_service)

        self.chat_completion_service = chat_service

    async def execute_prompt(self, command: ExecutePromptCommand) -> LLMResult:

        history = ChatHistory()
        history.add_user_message(command.prompt)

        settings = OllamaChatPromptExecutionSettings(
                service_id=service_id,
                options={
                    "temperature": 0.8,
                },
            )

        result = await self.chat_completion_service.get_chat_message_content(
            history, settings
        )

        # Print the AI's response
        result = LLMResult()
        result.content = result.content        
        return result
