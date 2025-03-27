
from pydantic import BaseModel, field_validator


class UserMessage(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def validate_message(cls, message) -> str:
        if message is None or len(message) == 0:
            raise ValueError("Invalid message")
        return message

    def format_message(self) -> str:
        return "Utilisateur : " + self.message


class AssistantMessage(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def validate_message(cls, message) -> str:
        if message is None or len(message) == 0:
            raise ValueError("Invalid message")
        return message

    def format_message(self) -> str:
        return "Assistant : " + self.message
