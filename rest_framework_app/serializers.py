from rest_framework import serializers
from .models import ProductTable

class ProductTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = '__all__'