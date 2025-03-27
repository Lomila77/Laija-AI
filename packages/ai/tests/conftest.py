import pytest
from fastapi.testclient import TestClient
from src.service import app
from src.llm.base.BaseAssistant import BaseAssistant


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def personalize_request():
    """JSON personnalize request"""
    return {
        'message': 'message test',
        'llm_name': 'name test',
        'adjectifs': ['ad1', 'ad2'],
    }


@pytest.fixture
def empty_adj_personalize_request(personalize_request):
    """JSON personalize request with empty array for adjectifs"""
    personalize_request['adjectifs'] = []
    return personalize_request


@pytest.fixture
def api_request():
    """JSON api request"""
    return {
        'message': 'message test',
    }


@pytest.fixture
def empty_msg_api_request(api_request):
    """JSON api request with empty message"""
    api_request['message'] = ''
    return api_request


@pytest.fixture
def base_assistant():
    return BaseAssistant