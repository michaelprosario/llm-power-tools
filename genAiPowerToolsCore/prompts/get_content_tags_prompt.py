from genAiPowerToolsCore.prompts.base_prompt import BasePrompt

class GetContentTagsPrompt(BasePrompt):
    def __init__(self, text: str):
        self.text = text

    def getText(self) -> str:
        return f"Get hash tags for the text appropriate to social media.  Return as json array: {self.text}"
    
