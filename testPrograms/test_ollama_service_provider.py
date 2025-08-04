import sys
import os

# Add the parent directory to the path to import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from genAiPowerToolsCore.llm_services import ModelConfig, ExecutePromptCommand
from genAiPowerToolsOllama.ollama_service_provider import OllamaServiceProvider





def test_simple_prompt():
    """Test executing a simple prompt."""
    print("\n=== Testing Simple Prompt Execution ===")
    
    try:
        # Create model configuration
        model_config = ModelConfig(
            model_name="gemma3:4b", 
            temperature=0.7,
            max_tokens=100
        )
        
        print(f"Model Config: {model_config}")
        print(f"Model Config Dict: {model_config.to_dict()}")
        
        # Create service provider
        provider = OllamaServiceProvider(model_config)
        print(f"Provider created: {provider}")
        
        # Create command
        command = ExecutePromptCommand(
            prompt="Tell me a joke about minecraft",
            context={"test": "basic_functionality"}
        )

        print(f"Command created with prompt: '{command.prompt}'")
                
        print(f"Executing prompt: '{command.prompt}'")
        result = provider.execute_prompt(command)
        
        print(f"Success: {result.success}")
        print(f"Content: {result.content}")
        print(f"Message: {result.message}")
        print(f"Errors: {result.errors}")
        
    except Exception as e:
        print(f"Error during simple prompt test: {e}")


def main():
    """Run all tests."""
    print("Starting Ollama Service Provider Tests")
    print("=" * 50)
    
    # Check if Ollama is running
    print("Note: Make sure Ollama is running (ollama serve) and models are installed")
    print("Install test model with: ollama pull llama3.2:1b")
    print()
    
    try:
        test_simple_prompt()
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except KeyboardInterrupt:
        print("\nTests interrupted by user")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()