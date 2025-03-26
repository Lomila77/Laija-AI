import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.models import AI


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_1(django_user_model):
    return django_user_model.objects.create_user(
        username='testuser',
        password='testpass123'
    )


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        username="anotheruser",
        password="anotherpass123"
    )


@pytest.fixture
def user_1_client(client: APIClient, user_1: User):
    client.force_authenticate(user=user_1)
    return client


@pytest.fixture
def user_2_client(client: APIClient, user_2: User):
    client.force_authenticate(user=user_2)
    return client


@pytest.fixture
def create_ai():
    def make_ai(creator, name="Test AI"):
        return AI.objects.create(name=name, creator=creator)
    return make_ai
