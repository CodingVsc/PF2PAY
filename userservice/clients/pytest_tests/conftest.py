import pytest
from rest_framework.test import APIClient
from clients.models import User, Reviews


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    user = User.objects.create_user(
        email='test@example.com',
        username='testuser',
        password='testpassword'
    )
    return user


@pytest.fixture
def test_review(test_user):
    return Reviews.objects.create(name='Test Review', user_id=test_user)


@pytest.fixture
def new_user_data():
    return {
        'email': 'newuser@example.com',
        'username': 'newuser',
        'password1': 'newpassword',
        'password2': 'newpassword',
    }


@pytest.fixture
def password_data():
    return {
        'old_password': 'testpassword',
        'new_password': 'newtestpassword',
    }