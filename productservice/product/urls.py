from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ListGameApiView, ListProductApiView, ProductDetailEntryGroupView, ProductCreateApiView


app_name = 'product'
router = DefaultRouter()
router.register(r'games', ListGameApiView, basename='games')

urlpatterns = [
    path('games/<int:pk>/products/', ListProductApiView.as_view(), name='products'),
    path('product_detail/<int:pk>/', ProductDetailEntryGroupView.as_view, name='product_detail'),
    path('product_create/', ProductCreateApiView.as_view(), name='product_create'),
] + router.urls
