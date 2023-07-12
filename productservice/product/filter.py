from django_filters import rest_framework as filters
from .models import ProductBase


class ProductFilter(filters.FilterSet):
    priceFrom = filters.NumberFilter(field_name="price", lookup_expr='gte')
    priceTo = filters.NumberFilter(field_name="price", lookup_expr='lte')
    platform = filters.CharFilter(field_name="platform")
    isOnline = filters.BooleanFilter(field_name="is_online")
    category_param = filters.CharFilter(field_name="params")
    key_param = filters.CharFilter(field_name="params")
    value_param = filters.CharFilter(field_name="params")


    class Meta:
        model = ProductBase
        fields = ['priceFrom', 'priceTo', 'platform', 'category_param', 'key_param', 'value_param']