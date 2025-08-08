class TikTokenEstimator():
    """Token estimator using tiktoken library (if available)."""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        """
        Initialize with specific model encoding.
        
        Args:
            model_name: Model name to get appropriate encoding
        """
        self.model_name = model_name
        self._encoding = None
        self._init_encoding()
    
    def _init_encoding(self):
        """Initialize tiktoken encoding if available."""
        try:
            import tiktoken
            self._encoding = tiktoken.encoding_for_model(self.model_name)
        except ImportError:
            print("Warning: tiktoken not available. Install with: pip install tiktoken")
            self._encoding = None
        except Exception as e:
            print(f"Warning: Could not load encoding for {self.model_name}: {e}")
            self._encoding = None
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate tokens using tiktoken if available, fallback to simple estimation."""
        if not text:
            return 0
            
        if self._encoding:
            return len(self._encoding.encode(text))
        else:
            # Fallback to simple character-based estimation
            return max(1, int(len(text) / 4.0))