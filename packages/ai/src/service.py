from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from src.api.request_dto import APIRequestDTO, PersonalizeRequestDTO
import os
from src.llm.personalize.PersonalizeAssistant import PersonalizeAssistant
from src.llm.base.BaseAssistant import BaseAssistant

path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv()

app = FastAPI()


# TODO: rename HF_TOKEN to HF_API_KEY
@app.post("/personalize")
async def personalize(body: PersonalizeRequestDTO):
    assistant = PersonalizeAssistant(
        message=body.message,
        adjectifs=body.adjectifs,
        name=body.llm_name,
    )
    try:
        response = await assistant.call_llm(token=os.getenv("HF_TOKEN"))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generic")
async def generic(body: APIRequestDTO):
    assistant = BaseAssistant(message=body.message,)
    try:
        response = await assistant.call_llm(token=os.getenv("HF_TOKEN"))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
