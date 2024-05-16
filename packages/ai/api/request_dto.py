from pydantic import BaseModel, field_validator

class APIRequestDTO(BaseModel):
    message: str
    #username: str

class PersonalizeRequestDTO(APIRequestDTO):
    llm_name: str = "Lucarance"
    adjectifs: list[str]

    @field_validator("adjectifs")
    @classmethod
    def validate_adjectifs(cls, adjectifs) -> list[str]:
        if adjectifs is None:
            raise ValueError("Need adjectifs")
        return adjectifs
