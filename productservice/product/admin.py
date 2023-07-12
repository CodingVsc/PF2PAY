from django.contrib import admin

from .models import Game, ProductBase


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'is_visibility')
    list_display_links = ('game_name',)


@admin.register(ProductBase)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'description',
                    'created_at', 'modified_at', 'price',
                    'is_active', 'is_banned',
                    'platform', 'params', 'game_id')
    list_filter = ('game_id__game_name',)
    search_fields = ('game_id__game_name', 'short_description', 'is_banned')
