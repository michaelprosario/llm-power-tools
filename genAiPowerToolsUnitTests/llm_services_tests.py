import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from genAiPowerToolsCore.llm_services import (
    AppResult, 
    ExecutePromptCommand, 
    LLMResult, 
    ModelConfig, 
    LLMServiceProvider,
    LLMService
)


class TestAppResult(unittest.TestCase):
    
    def test_app_result_success_creation(self):
        result = AppResult(success=True, message="Success")
        self.assertTrue(result.success)
        self.assertEqual(result.message, "Success")
        self.assertEqual(result.errors, [])
    
    def test_app_result_failure_creation(self):
        errors = ["Error 1", "Error 2"]
        result = AppResult(success=False, message="Failed", errors=errors)
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Failed")
        self.assertEqual(result.errors, errors)
    
    def test_app_result_default_values(self):
        result = AppResult(success=True)
        self.assertEqual(result.message, "")
        self.assertEqual(result.errors, [])
    
    def test_app_result_to_dict(self):
        result = AppResult(success=True, message="Test", errors=["error1"])
        expected = {
            "success": True,
            "message": "Test",
            "errors": ["error1"]
        }
        self.assertEqual(result.to_dict(), expected)
    
    def test_app_result_repr(self):
        result = AppResult(success=False, message="Test", errors=["error"])
        expected = "AppResult(success=False, message=Test, errors=['error'])"
        self.assertEqual(repr(result), expected)


class TestLLMResult(unittest.TestCase):
    
    def test_llm_result_creation(self):
        result = LLMResult()
        self.assertTrue(result.success)
        self.assertEqual(result.content, "")
    
    def test_llm_result_inherits_from_app_result(self):
        result = LLMResult()
        self.assertIsInstance(result, AppResult)


class TestExecutePromptCommand(unittest.TestCase):
    
    def test_execute_prompt_command_creation(self):
        prompt = "Test prompt"
        context = {"key": "value"}
        command = ExecutePromptCommand(prompt, context)
        
        self.assertEqual(command.prompt, prompt)
        self.assertEqual(command.context, context)


class TestModelConfig(unittest.TestCase):
    
    def test_model_config_required_model_name(self):
        config = ModelConfig("gpt-4")
        self.assertEqual(config.model_name, "gpt-4")
    
    def test_model_config_with_core_parameters(self):
        config = ModelConfig(
            "gpt-4",
            temperature=0.7,
            max_tokens=1000,
            top_p=0.9,
            top_k=50
        )
        self.assertEqual(config.model_name, "gpt-4")
        self.assertEqual(config.temperature, 0.7)
        self.assertEqual(config.max_tokens, 1000)
        self.assertEqual(config.top_p, 0.9)
        self.assertEqual(config.top_k, 50)
    
    def test_model_config_with_api_parameters(self):
        config = ModelConfig(
            "gpt-4",
            api_key="test-key",
            base_url="https://api.test.com",
            timeout=30
        )
        self.assertEqual(config.api_key, "test-key")
        self.assertEqual(config.base_url, "https://api.test.com")
        self.assertEqual(config.timeout, 30)
    
    def test_model_config_with_local_parameters(self):
        config = ModelConfig(
            "llama-2",
            model_path="/path/to/model",
            device="cuda",
            batch_size=4
        )
        self.assertEqual(config.model_path, "/path/to/model")
        self.assertEqual(config.device, "cuda")
        self.assertEqual(config.batch_size, 4)
    
    def test_model_config_with_advanced_parameters(self):
        stop_sequences = ["\n", "END"]
        config = ModelConfig(
            "gpt-4",
            stop_sequences=stop_sequences,
            seed=42,
            system_prompt="You are a helpful assistant"
        )
        self.assertEqual(config.stop_sequences, stop_sequences)
        self.assertEqual(config.seed, 42)
        self.assertEqual(config.system_prompt, "You are a helpful assistant")
    
    def test_model_config_with_custom_parameters(self):
        config = ModelConfig(
            "custom-model",
            custom_param1="value1",
            custom_param2=123
        )
        self.assertEqual(config.custom_params["custom_param1"], "value1")
        self.assertEqual(config.custom_params["custom_param2"], 123)    

class MockLLMServiceProvider(LLMServiceProvider):
    def __init__(self, mock_response="Mock response"):
        self.mock_response = mock_response
        self.last_command = None
        self.last_config = None
    
    def execute_prompt(self, command: ExecutePromptCommand, model_config: ModelConfig) -> LLMResult:
        self.last_command = command
        self.last_config = model_config
        
        result = LLMResult()
        result.content = self.mock_response
        return result


class TestLLMService(unittest.TestCase):
    
    def setUp(self):
        self.model_config = ModelConfig("test-model", temperature=0.7)
        self.mock_provider = MockLLMServiceProvider()
        self.llm_service = LLMService(self.model_config, self.mock_provider)
    
    def test_llm_service_creation(self):
        self.assertEqual(self.llm_service.model_config, self.model_config)
        self.assertEqual(self.llm_service.llm_service_provider, self.mock_provider)
    
    def test_llm_service_invalid_model_config(self):
        with self.assertRaises(ValueError):
            LLMService("not-a-model-config", self.mock_provider)
    
    def test_execute_prompt_success(self):
        command = ExecutePromptCommand("Test prompt", {"context": "test"})
        result = self.llm_service.execute_prompt(command)
        
        self.assertTrue(result.success)
        self.assertEqual(result.content, "Mock response")
        self.assertEqual(self.mock_provider.last_command, command)
        self.assertEqual(self.mock_provider.last_config, self.model_config)
    
    def test_execute_prompt_invalid_prompt_none(self):
        command = ExecutePromptCommand(None, {"context": "test"})
        result = self.llm_service.execute_prompt(command)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Invalid prompt.")
    
    def test_execute_prompt_invalid_prompt_empty(self):
        command = ExecutePromptCommand("", {"context": "test"})
        result = self.llm_service.execute_prompt(command)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Invalid prompt.")
    
    def test_execute_prompt_invalid_prompt_non_string(self):
        command = ExecutePromptCommand(123, {"context": "test"})
        result = self.llm_service.execute_prompt(command)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Invalid prompt.")


class TestLLMServiceProvider(unittest.TestCase):
    
    def test_llm_service_provider_is_abstract(self):
        with self.assertRaises(TypeError):
            LLMServiceProvider()
    
    def test_mock_provider_implementation(self):
        provider = MockLLMServiceProvider("Test response")
        config = ModelConfig("test-model")
        command = ExecutePromptCommand("Test prompt", {"context": "test"})
        
        result = provider.execute_prompt(command, config)
        
        self.assertIsInstance(result, LLMResult)
        self.assertEqual(result.content, "Test response")


if __name__ == '__main__':
    unittest.main()