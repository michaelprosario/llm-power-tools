from pyparsing import ABC, abstractmethod

class BasePrompt(ABC):
    """
    Base class for all prompts.
    """
    @abstractmethod
    def getText(self) -> str:
        """
        Returns the text of the prompt.
        """
        pass