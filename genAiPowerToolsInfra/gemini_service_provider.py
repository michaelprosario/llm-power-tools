
from semantic_kernel import Kernel
from genAiPowerToolsCore.llm_services import ExecutePromptCommand, LLMResult, LLMServiceProvider, ModelConfig
from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatCompletion
from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory

class GeminiServiceProvider(LLMServiceProvider):
    def __init__(self, model_config: ModelConfig):
        super().__init__(model_config)

        # use a gemini flash model
        model_id = model_config.model_name or "gemini-1.5-flash"  # Default model ID if not specified   

        self.kernel = Kernel()
        self.chat_completion_service = GoogleAIChatCompletion(
           gemini_model_id=model_id,
           api_key=model_config.api_key
        )

        self.kernel.add_service(self.chat_completion_service)

    def getKernel(self):
        return self.kernel

    async def execute_prompt(self, command: ExecutePromptCommand) -> LLMResult:

        chat_history = ChatHistory()
        chat_history.add_user_message(command.prompt)

        execution_settings = GoogleAIChatPromptExecutionSettings()

        chat_output = await self.chat_completion_service.get_chat_message_content(
            chat_history=chat_history,
            settings=execution_settings
        )

        response = LLMResult()
        response.content = chat_output.content
        return response
    