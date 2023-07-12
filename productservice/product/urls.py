from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ListGameApiView, ListProductApiView, ProductDetailEntryGroupView, ProductCreateApiView
from . import views

app_name = 'product'
router = DefaultRouter()
router.register(r'games', ListGameApiView, basename='games')
# urlpatterns = [
#     # path('home/', ListGameApiView.as_view(), name='home'),
#     path('all_product/<slug:slug_field>/', AllProductApiView.as_view(), name='all_product'),
#     path('get_user_avatar/<slug:slug_field>/', views.get_user_avatar, name='get_user_avatar'),
#     path('game/<int:pk>/', ListProductApiView.as_view(), name='game'),
#     path('game-params/<int:pk>/', views.GameParamRetrieveApiView.as_view(), name='game_param'),
#     path('game-name/<int:pk>/', views.GameNameRetrieveApiView.as_view(), name='game_name'),
#     # path('create/', views.ListGameApiView, name='product_create'),
# ] + router.urls

urlpatterns = [
    path('games/<int:pk>/products/', ListProductApiView.as_view(), name='products'),
    path('product_detail/<int:pk>/', ProductDetailEntryGroupView.as_view, name='product_detail'),
    path('product_create/', ProductCreateApiView.as_view(), name='product_create'),
] + router.urls
