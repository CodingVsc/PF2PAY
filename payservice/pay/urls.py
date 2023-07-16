from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.UserCreateApiView.as_view(), name='signup'),
]