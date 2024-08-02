from llm.base.BaseAssistant import BaseAssistant
from llm.utils.prompts import Prompt
from llm.personalize.prompt.personalize import PERSONALIZE_PROMPT

class PersonalizeAssistant(BaseAssistant):
    unformatted_prompt: dict = PERSONALIZE_PROMPT
    adjectifs: list[str] = None
    name: str = "Lucarance"

    @property
    def prompt(self) -> str:
        prompt = Prompt(
            system_prompt=self.unformatted_prompt["system_prompt"],
            name=self.name,
            instructions=self.unformatted_prompt["instructions"],
            message=self.message,
            examples=self.unformatted_prompt["examples"],
            adjectifs=self.adjectifs,
        )
        return prompt.format_prompt()
