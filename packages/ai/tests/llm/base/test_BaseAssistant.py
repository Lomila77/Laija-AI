import pytest
from src.llm.base.BaseAssistant import BaseAssistant
from unittest.mock import Mock, patch, AsyncMock
import aiohttp


def test_validate_empty_message():
    message = ""
    with pytest.raises(ValueError) as exc_info:
        BaseAssistant(message=message)
    assert "Invalid message" in str(exc_info.value)
