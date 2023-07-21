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