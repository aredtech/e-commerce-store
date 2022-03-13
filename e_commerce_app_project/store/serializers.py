from decimal import Decimal
from rest_framework import serializers

from .models import Collection, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "unit_price", "price_after_tax", "stock", "slug", "collection"]

    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]

    products_count = serializers.IntegerField(required = False)