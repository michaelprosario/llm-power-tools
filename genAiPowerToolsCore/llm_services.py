import abc

class AppResult:
    def __init__(self, success, message=None, errors=[]):
        self.success = success
        self.message = message if message is not None else ""
        self.errors = errors if errors is not None else []

    def __repr__(self):
        return f"AppResult(success={self.success}, message={self.message}, errors={self.errors})"
    
    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "errors": self.errors
        }

class ExecutePromptCommand:
    def __init__(self, prompt, context):
        self.prompt = prompt        
        self.context = context        

class LLMResult(AppResult):
    def __init__(self, success=True, message=None, errors=[]):
        super().__init__(success=success, message=message, errors=errors)
        self.content = ""


class ModelConfig:
    def __init__(self, model_name: str, **kwargs):
        # Required parameter
        self.model_name = model_name
        
        # Core model parameters (optional)
        self.temperature = kwargs.get('temperature')
        self.max_tokens = kwargs.get('max_tokens')
        self.top_p = kwargs.get('top_p')
        self.top_k = kwargs.get('top_k')
        self.frequency_penalty = kwargs.get('frequency_penalty')
        self.presence_penalty = kwargs.get('presence_penalty')
        
        # API/Connection configuration (optional)
        self.api_key = kwargs.get('api_key')
        self.base_url = kwargs.get('base_url')
        self.endpoint = kwargs.get('endpoint')
        self.timeout = kwargs.get('timeout')
        self.max_retries = kwargs.get('max_retries')
        self.rate_limit = kwargs.get('rate_limit')
        
        # Local hosting specific (optional)
        self.model_path = kwargs.get('model_path')
        self.device = kwargs.get('device')
        self.gpu_memory_fraction = kwargs.get('gpu_memory_fraction')
        self.batch_size = kwargs.get('batch_size')
        self.num_threads = kwargs.get('num_threads')
        
        # Advanced parameters (optional)
        self.stop_sequences = kwargs.get('stop_sequences')
        self.seed = kwargs.get('seed')
        self.system_prompt = kwargs.get('system_prompt')
        self.context_window = kwargs.get('context_window')
        self.streaming = kwargs.get('streaming')
        
        # Store any additional custom parameters
        self.custom_params = {k: v for k, v in kwargs.items() 
                            if k not in self.__dict__}

class LLMServiceProvider(abc.ABC):

    def __init__(self, model_config: ModelConfig):
        # ensure model_config is an instance of ModelConfig
        if not isinstance(model_config, ModelConfig):
            raise ValueError("model_config must be an instance of ModelConfig")

        self.model_config = model_config

    @abc.abstractmethod
    def execute_prompt(self, command: ExecutePromptCommand) -> LLMResult:
        """Execute a prompt with the LLM and return the response."""
        pass    
    
    def to_dict(self):
        """Convert the config to a dictionary, excluding None values."""
        result = {}
        for key, value in self.__dict__.items():
            if key != 'custom_params' and value is not None:
                result[key] = value
        # Add custom parameters
        result.update(self.custom_params)
        return result
    
    def __repr__(self):
        return f"ModelConfig(model_name='{self.model_name}', {len(self.to_dict())-1} parameters)"


class LLMService():
    def __init__(self, model_config: ModelConfig, llm_service_provider: LLMServiceProvider):
        # ensure model_config is an instance of ModelConfig
        if not isinstance(model_config, ModelConfig):
            raise ValueError("model_config must be an instance of ModelConfig")

        self.model_config = model_config
        self.llm_service_provider = llm_service_provider

    def execute_prompt(self, command: ExecutePromptCommand) -> LLMResult:
        # ensure prompt is well defined
        if command.prompt == None or not command.prompt or not isinstance(command.prompt, str):
            return LLMResult(success=False, message="Invalid prompt.")

        # Call the LLM service provider to get a response
        response = self.llm_service_provider.execute_prompt(command, self.model_config)
        return response
