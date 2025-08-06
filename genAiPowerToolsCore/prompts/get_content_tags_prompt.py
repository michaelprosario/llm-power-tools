from genAiPowerToolsCore.prompts.base_prompt import BasePrompt

class GetContentTagsPrompt(BasePrompt):
    def __init__(self, text: str):
        self.text = text

    def getText(self) -> str:
        return f"Get content tags for the text appropriate to linked-in.  Return as JSON array: {self.text}"
    
