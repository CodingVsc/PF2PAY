import pytest
from django.urls import reverse, resolve
from clients import views


@pytest.mark.django_db
def test_signup_url():
    url = reverse('users:signup')
    assert resolve(url).view_name == 'users:signup'
    assert views.SignUpApiView in resolve(url).func.view_class.mro()


@pytest.mark.django_db
def test_profile_detail_url(test_user):
    url = reverse('users:profile', kwargs={'pk': test_user.pk})
    assert resolve(url).view_name == 'users:profile'
    assert views.ProfileDetailApiView in resolve(url).func.view_class.mro()


@pytest.mark.django_db
def test_edit_profile_url(test_user):
    url = reverse('users:edit_profile', kwargs={'pk': test_user.pk})
    assert resolve(url).view_name == 'users:edit_profile'
    assert views.EditProfileApiView in resolve(url).func.view_class.mro()


@pytest.mark.django_db
def test_change_password_url():
    url = reverse('users:edit_password')
    assert resolve(url).view_name == 'users:edit_password'
    assert views.ChangePasswordApiView in resolve(url).func.view_class.mro()


@pytest.mark.django_db
def test_reviews_entry_group_url(test_user):
    url = reverse('reviews-entry-group', kwargs={'pk': test_user.pk})
    assert resolve(url).view_name == 'reviews-entry-group'
    assert views.ReviewsEntryGroup in resolve(url).func.view_class.mro()