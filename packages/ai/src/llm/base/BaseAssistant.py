from pydantic import BaseModel, field_validator
from src.llm.base.prompt.generic import GENERIC_PROMPT
from src.llm.utils.prompts import Prompt
import aiohttp


class BaseAssistant(BaseModel):
    message: str
    unformatted_prompt: dict = GENERIC_PROMPT
    model: str = "mistralai/Mistral-7B-Instruct-v0.2"
    url: str = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    parameters: dict[str, int] = {
        "max_new_tokens": 100,
        "temperature": 0.5,
        "top_k": 50,
        "repetition_penalty": 1.2,
    }
    options: dict[str, bool] = {"wait_for_model": True}

    @field_validator("message")
    @classmethod
    def validate_message(cls, message: str) -> str:
        if message is None or message == "":
            raise ValueError("Invalid message")
        return message

    @property
    def prompt(self) -> str:
        prompt = Prompt(
            system_prompt=self.unformatted_prompt["system_prompt"],
            message=self.message,
            examples=self.unformatted_prompt["examples"],
            adjectifs=self.unformatted_prompt["adjectifs"],
            name=self.unformatted_prompt["name"]
        )
        return prompt.format_prompt()

    async def call_llm(self, token: str):
        # TODO: recuperer le token ici
        headers = {
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "inputs": self.prompt,
            "options": self.options,
            "parameters": self.parameters,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.url, headers=headers, json=payload
                ) as response:
                    result = await response.text()
                    return result
        except aiohttp.ClientError as e:
            raise Exception(f"Erreur lors de la requête HTTP: {str(e)}")
        except Exception as e:
            raise Exception(f"Erreur inattendue: {str(e)}")
