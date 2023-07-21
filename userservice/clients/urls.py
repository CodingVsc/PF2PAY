from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'users'

router = DefaultRouter()
router.register(r'reviews-entry-group', views.ReviewsEntryGroup, basename='reviews-entry-group')

urlpatterns = [
    path('signup/', views.SignUpApiView.as_view(), name='signup'),
    path('profile/<slug:pk>/', views.ProfileDetailApiView.as_view(), name='profile'),
    path('edit-profile/<slug:pk>/', views.EditProfileApiView.as_view(), name='edit_profile'),
    path('edit-password/', views.ChangePasswordApiView.as_view(), name='edit_password'),
] + router.urls
