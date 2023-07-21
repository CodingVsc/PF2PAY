import pytest
from django.urls import reverse
from rest_framework import status
from product.models import Game, ProductBase
from product.serializers import GameSerializer, ProductSerializer


@pytest.mark.django_db
def test_get_all_games(api_client, game):
    url = reverse('product:games-list')
    response = api_client.get(url)
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.django_db
def test_get_all_products_for_game(api_client, game, product):
    url = reverse('product:products', kwargs={'pk': game.pk})
    response = api_client.get(url)
    products = ProductBase.objects.filter(game_id=game, is_active=True)
    serializer = ProductSerializer(products, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.django_db
def test_create_product(api_client, game):
    url = reverse('product:product_create')
    new_product_data = {
        'short_description': 'New Test Product',
        'description': 'New Test Product Description',
        'price': 9.99,
        'is_active': True,
        'platform': 'PC',
        'params': {},
        'game_id': game.pk,
        'user_id': None,
        'buyer_id': None,
    }
    response = api_client.post(url, new_product_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert ProductBase.objects.count() == 1


@pytest.mark.django_db
def test_delete_product(api_client, product):
    url = reverse('product:product_detail', kwargs={'pk': product.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not ProductBase.objects.filter(pk=product.pk).exists()
