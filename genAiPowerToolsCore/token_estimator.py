import re
from typing import Optional
from abc import ABC, abstractmethod


class TokenEstimator(ABC):
    """Abstract base class for token size estimation."""
    
    @abstractmethod
    def estimate_tokens(self, text: str) -> int:
        """Estimate the number of tokens in the given text."""
        pass


class SimpleTokenEstimator(TokenEstimator):
    """Simple token estimator using basic word and character counting."""
    
    def __init__(self, chars_per_token: float = 4.0):
        """
        Initialize with average characters per token.
        
        Args:
            chars_per_token: Average number of characters per token (default: 4.0 for GPT models)
        """
        self.chars_per_token = chars_per_token
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate tokens using character count divided by average chars per token."""
        if not text:
            return 0
        return max(1, int(len(text) / self.chars_per_token))


class WordBasedTokenEstimator(TokenEstimator):
    """Token estimator based on word and punctuation counting."""
    
    def __init__(self, word_to_token_ratio: float = 0.75):
        """
        Initialize with word-to-token ratio.
        
        Args:
            word_to_token_ratio: Ratio of tokens to words (default: 0.75, meaning 100 words ≈ 75 tokens)
        """
        self.word_to_token_ratio = word_to_token_ratio
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate tokens based on word count and punctuation."""
        if not text:
            return 0
            
        # Count words (sequences of alphanumeric characters)
        words = len(re.findall(r'\b\w+\b', text))
        
        # Count punctuation and special characters
        punctuation = len(re.findall(r'[^\w\s]', text))
        
        # Estimate tokens: words contribute based on ratio, punctuation usually 1:1
        estimated_tokens = int(words * self.word_to_token_ratio) + punctuation
        
        return max(1, estimated_tokens)


class TikTokenEstimator(TokenEstimator):
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


class TokenSizeEstimator:
    """Main token size estimator that can use different estimation strategies."""
    
    def __init__(self, estimator: Optional[TokenEstimator] = None):
        """
        Initialize with a specific estimator strategy.
        
        Args:
            estimator: TokenEstimator instance. If None, uses SimpleTokenEstimator.
        """
        self.estimator = estimator or SimpleTokenEstimator()
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate the number of tokens in the given text."""
        return self.estimator.estimate_tokens(text)
    
    def estimate_cost(self, text: str, cost_per_1k_tokens: float) -> float:
        """
        Estimate the cost for processing the given text.
        
        Args:
            text: Input text
            cost_per_1k_tokens: Cost per 1000 tokens
            
        Returns:
            Estimated cost in the same currency unit as cost_per_1k_tokens
        """
        tokens = self.estimate_tokens(text)
        return (tokens / 1000.0) * cost_per_1k_tokens
    
    def get_token_info(self, text: str) -> dict:
        """
        Get comprehensive token information for the text.
        
        Returns:
            Dictionary with token count, character count, and basic stats
        """
        tokens = self.estimate_tokens(text)
        chars = len(text)
        words = len(text.split()) if text else 0
        
        return {
            "estimated_tokens": tokens,
            "character_count": chars,
            "word_count": words,
            "chars_per_token": chars / tokens if tokens > 0 else 0,
            "estimator_type": self.estimator.__class__.__name__
        }


# Convenience functions for quick usage
def estimate_tokens(text: str, method: str = "simple") -> int:
    """
    Quick function to estimate tokens.
    
    Args:
        text: Input text
        method: Estimation method ("simple", "word", "tiktoken")
        
    Returns:
        Estimated token count
    """
    if method == "simple":
        estimator = SimpleTokenEstimator()
    elif method == "word":
        estimator = WordBasedTokenEstimator()
    elif method == "tiktoken":
        estimator = TikTokenEstimator()
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return estimator.estimate_tokens(text)