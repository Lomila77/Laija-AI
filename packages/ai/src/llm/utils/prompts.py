from pydantic import BaseModel, field_validator, Field
from src.llm.utils.messages.user_messages import UserMessage


class Prompt(BaseModel):
    system_prompt: str
    name: str = Field(default="Lucarance")
    instructions: str
    examples: str = None
    message: str
    adjectifs: list[str] = Field(default=None)

    @field_validator("system_prompt")
    @classmethod
    def validate_prompt(cls, system_prompt) -> str:
        if system_prompt is None:
            raise ValueError("Need system prompt.")
        return system_prompt

    @field_validator("message")
    @classmethod
    def validate_message(cls, message) -> str:
        if message is None or len(message) == 0:
            raise ValueError("Need message")
        return UserMessage(message=message).format_message()

    @field_validator("instructions")
    @classmethod
    def validate_instructions(cls, instructions) -> str:
        if instructions is None:
            raise ValueError("Need instructions")
        return instructions

    def format_prompt(self) -> str:
        prompt = self.system_prompt
        prompt += self.format_name()
        prompt += self.instructions
        prompt += self.format_adjectifs() if self.adjectifs else ""
        prompt += self.examples if self.examples else ""
        prompt += self.message
        prompt += self.format_response()
        return prompt

    def format_adjectifs(self) -> str:
        formatted_adjectifs = ""
        for each_adjectif in self.adjectifs:
            formatted_adjectifs += f"- {each_adjectif}\n"
        return formatted_adjectifs

    def format_name(self) -> str:
        return f"Ton prénom est {self.name}.\n" if self.name else ""

    def format_message(self) -> str:
        return "### Question :\n" + self.message.format_message()

    def format_response(self) -> str:
        return "\nAssistant : "
