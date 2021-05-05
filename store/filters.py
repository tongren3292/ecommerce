import django_filters
from django_filters import CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    product_name = CharFilter(field_name='name')
    class Meta:
        model = Product
        fields ='__all__'
        exclude = ['image', 'name']
