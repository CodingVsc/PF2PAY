from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('check-auth/', views.check_auth, name='check-auth'),
#     path('user_detail/<slug:pk>/', views.ProfileUserDetail.as_view(), name='user_detail'),
#     path('editprofile/', views.editprofile, name='edit_profile'),
#     path('editpassword/', views.editpassword, name='edit_password'),
#     path('me/', views.me, name='login')
# ]

urlpatterns = [
    path('signup/', views.SignUpApiView.as_view(), name='signup'),
    path('profile/<slug:pk>/', views.ProfileDetailApiView.as_view(), name='profile'),
    path('edit-profile/<slug:pk>/', views.EditProfileApiView.as_view, name='edit_profile'),
    path('edit-password/', views.ChangePasswordApiView.as_view(), name='edit_password'),
]