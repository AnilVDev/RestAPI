from product.models import Product
from rest_framework import serializers

class CbvProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'