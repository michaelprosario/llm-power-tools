from genAiPowerToolsCore.prompts.base_prompt import BasePrompt

class GetSummaryPrompt(BasePrompt):
    def __init__(self, text: str):
        self.text = text

    def getText(self) -> str:
        return f"Summary of the text: {self.text}."
    
