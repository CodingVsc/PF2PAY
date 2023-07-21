import pytest
from rest_framework.test import APIClient
from product.models import Game, ProductBase


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def game():
    return Game.objects.create(game_name='Test Game', is_visibility=True, params={})


@pytest.fixture
def product(game):
    return ProductBase.objects.create(
        short_description='Test Product',
        description='Test Product Description',
        price=19.99,
        is_active=True,
        platform='PC',
        params={},
        game_id=game,
        user_id=None,
        buyer_id=None,
    )