from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpApiView.as_view(), name='signup'),
    path('profile/<slug:pk>/', views.ProfileDetailApiView.as_view(), name='profile'),
    path('edit-profile/<slug:pk>/', views.EditProfileApiView.as_view(), name='edit_profile'),
    path('edit-password/', views.ChangePasswordApiView.as_view(), name='edit_password'),
]