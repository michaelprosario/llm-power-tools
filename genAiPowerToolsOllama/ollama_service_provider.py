
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig

import asyncio
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.prompt_execution_settings import PromptExecutionSettings
from semantic_kernel.functions.function_choice_behavior import FunctionChoiceBehavior # For auto function calling
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

class OllamaServiceProvider(LLMServiceProvider):
    def __init__(self, model_config: ModelConfig):
        super().__init__(model_config)

        model_id = model_config.model_name or "llama2"  # Default model name if not specified   
        base_url = model_config.base_url or "http://localhost:11434"  # Default base URL if not specified

        # Create a kernel and add the Ollama chat completion service
        # In Python, this involves using Kernel.create_builder() and then adding the service.
        self.kernel = Kernel.create_builder().add_ollama_chat_completion(
            model_id=model_id,
            base_url=base_url
        ).build()

        self.chat_completion_service = self.kernel.get_required_service(OllamaChatCompletion)

    async def execute_prompt(self, command: ExecutePromptCommand) -> LLMResult:

        # todo - deal with history later
        #history.add_user_message(user_input)
        execution_settings = PromptExecutionSettings(            
            function_choice_behavior=FunctionChoiceBehavior.AUTO            
        )

        history = ChatHistory()
        history.add_user_message(command.prompt)

        result = await self.chat_completion_service.get_chat_message_content(
            history,
            settings=execution_settings,
            kernel=self.kernel
        )

        # Print the AI's response
        print(f"Assistant > {result.content}")

        result = LLMResult()
        result.content = result.content        
        return result
    