from rest_framework import serializers

from .models import Game, ProductBase


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        exclude = ('is_visibility',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductBase
        fields = ('short_description', 'description', 'created_at', 'price',
                  'is_active', 'platform', 'params',
                  'game_id', 'user_id')


