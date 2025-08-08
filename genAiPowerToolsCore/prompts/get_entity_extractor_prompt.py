from genAiPowerToolsCore.prompts.base_prompt import BasePrompt

class GetEntityExtractor(BasePrompt):
    def __init__(self, text: str, entities: str):
        self.text = text
        self.entities = entities

    def getText(self) -> str:
        return f"Extract entities like {self.entities} from the text and return as json: {self.text}"

