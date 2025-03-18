from django.test import TestCase
import pytest
from models import User, UserManager

# Create your tests here.
@pytest.mark.django_db
def test_create_user(username, password):
    obj = User.objects.create()