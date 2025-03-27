import pytest
import os
from unittest.mock import AsyncMock, patch
from src.llm.personalize.PersonalizeAssistant import PersonalizeAssistant
from src.llm.base.BaseAssistant import BaseAssistant


@patch.object(PersonalizeAssistant, 'call_llm', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_personalize_endpoint(
    mock_call_llm, client, personalize_request
):
    mock_call_llm.return_value = "Réponse personnalisée du LLM"

    response = client.post('/personalize', json=personalize_request)

    assert response.status_code == 200
    assert response.json() == "Réponse personnalisée du LLM"
    # TODO: Rename env key
    mock_call_llm.assert_called_once_with(token=os.getenv("HF_TOKEN"))


@patch.object(PersonalizeAssistant, 'call_llm', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_personalize_endpoint_error(
    mock_call_llm, client, personalize_request
):
    mock_call_llm.side_effect = Exception("Erreur test")
    response = client.post('/personalize', json=personalize_request)
    assert response.status_code == 500
    assert "Erreur test" in response.text


@patch.object(BaseAssistant, 'call_llm', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_generic_endpoint(
    mock_call_llm, client, api_request
):
    mock_call_llm.return_value = "Réponse personnalisée du LLM"

    response = client.post('/generic', json=api_request)

    assert response.status_code == 200
    assert response.json() == "Réponse personnalisée du LLM"
    # TODO: Rename env key
    mock_call_llm.assert_called_once_with(token=os.getenv("HF_TOKEN"))


@patch.object(BaseAssistant, 'call_llm', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_generic_endpoint_error(
    mock_call_llm, client, api_request
):
    mock_call_llm.side_effect = Exception("Erreur test")
    response = client.post('/generic', json=api_request)
    assert response.status_code == 500
    assert "Erreur test" in response.text
