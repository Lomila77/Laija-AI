import pytest
from src.api.request_dto import PersonalizeRequestDTO


def test_validate_adjectifs(personalize_request):
    test = PersonalizeRequestDTO(**personalize_request)
    assert len(test.adjectifs) == 2


def test_validate_empty_adjectifs(empty_adj_personalize_request):
    with pytest.raises(ValueError) as exc_info:
        PersonalizeRequestDTO(**empty_adj_personalize_request)
    assert "Need adjectifs" in str(exc_info.value)
