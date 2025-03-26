import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from api.models import AI


@pytest.mark.django_db
def test_create_user(client):
    url = reverse('register')
    user_data = {
        'username': 'testuser',
        'password': 'testpass123',
    }

    response = client.post(url, user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.get().username == 'testuser'


@pytest.mark.django_db
def test_create_user_invalid_data(client):
    url = reverse('register')
    user_data = {
        'username': '',
        'password': 'testpass123'
    }

    response = client.post(url, user_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_ai_list_create(
    user_1,
    user_1_client,
    user_2,
    create_ai,
):
    url = reverse("list-ai")
    user_1_ai = []
    user_2_ai = []
    user_1_ai.append(create_ai(user_1, "Auth AI 1"))
    user_1_ai.append(create_ai(user_1, "Auth AI 2"))
    user_2_ai.append(create_ai(user_2, "Another AI 1"))
    user_2_ai.append(create_ai(user_2, "Another AI 2"))
    response = user_1_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Auth AI 1"


@pytest.mark.django_db
def test_post_ai_list_create(
    user_1,
    user_1_client,
):
    ai_data = {
        'name': 'test',
        'back_story': 'test'
    }
    url = reverse('list-ai')
    response = user_1_client.post(url, ai_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert AI.objects.count() == 1
    assert AI.objects.get().name == 'test'


@pytest.mark.django_db
def test_unauthenticated_get_ai_list(client):
    url = reverse("list-ai")
    response = client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_unauthenticated_post_ai_list(client, user_1):
    url = reverse("list-ai")
    ai_data = {
        'name': 'test',
        'back_story': 'test'
    }
    response = client.post(url, ai_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_ai(user_1, user_1_client, create_ai):
    ai = create_ai(user_1)
    url = reverse("delete-ai", kwargs={"pk": ai.id})
    response = user_1_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert AI.objects.count() == 0


@pytest.mark.django_db
def test_delete_not_own_ai(user_1, user_2_client, create_ai):
    ai = create_ai(user_1)
    url = reverse("delete-ai", kwargs={"pk": ai.id})
    response = user_2_client.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert AI.objects.count() == 1


@pytest.mark.django_db
def test_delete_not_auth_ai(user_1, client, create_ai):
    ai = create_ai(user_1)
    url = reverse("delete-ai", kwargs={"pk": ai.id})
    response = client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert AI.objects.count() == 1


@pytest.mark.django_db
def test_delete_unknow_ai(user_1_client):
    url = reverse("delete-ai", kwargs={"pk": 45})
    response = user_1_client.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
