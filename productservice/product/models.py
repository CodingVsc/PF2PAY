from django.db import models
from django.core.validators import MinValueValidator


class Game(models.Model):
    game_name = models.CharField(max_length=50, blank=False)
    is_visibility = models.BooleanField(blank=False)
    params = models.JSONField(default=dict)


class ProductBase(models.Model):
    short_description = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)
    platform = models.CharField(max_length=10, default='PC')
    params = models.JSONField(default=dict)
    deleted = models.BooleanField(default=False, blank=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    user_id = models.UUIDField(null=True, default=None)
    buyer_id = models.UUIDField(null=True, default=None)




