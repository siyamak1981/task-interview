from rest_framework import serializers
from .models import Product, Rate


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rate
        fields=('ratenum',)
