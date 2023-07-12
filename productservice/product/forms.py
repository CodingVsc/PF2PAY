from django import forms

from .models import ProductBase


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductBase
        fields = ('short_description',
                  'description', 'price', 'user_id', 'game_id', 'params')