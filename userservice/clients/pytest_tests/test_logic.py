import pytest
from django.urls import reverse
from rest_framework import status
from clients.models import User, Reviews
from clients.serializers import UserSerializer, ReviewSerializer


@pytest.mark.django_db
def test_signup(api_client, new_user_data):
    url = reverse('users:signup')
    response = api_client.post(url, data=new_user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email='newuser@example.com').exists()


@pytest.mark.django_db
def test_get_profile(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    url = reverse('users:profile', kwargs={'pk': test_user.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    expected_data = UserSerializer(test_user).data
    assert response.data == expected_data


@pytest.mark.django_db
def test_update_profile(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    url = reverse('users:edit_profile', kwargs={'pk': test_user.pk})
    data = {'username': 'updated_username'}
    response = api_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    test_user.refresh_from_db()
    assert test_user.username == 'updated_username'


@pytest.mark.django_db
def test_change_password(api_client, test_user, password_data):
    api_client.force_authenticate(user=test_user)
    url = reverse('users:edit_password')
    response = api_client.put(url, data=password_data)
    assert response.status_code == status.HTTP_200_OK
    test_user.refresh_from_db()
    assert test_user.check_password('newtestpassword')


@pytest.mark.django_db
def test_get_reviews(api_client, test_user, test_review):
    api_client.force_authenticate(user=test_user)
    url = reverse('reviews-entry-group', kwargs={'pk': test_user.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    expected_data = ReviewSerializer(Reviews.objects.filter(user_id=test_user), many=True).data
    assert response.data == expected_data