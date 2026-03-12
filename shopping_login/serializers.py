from rest_framework import serializers
from .models import ShoppingLoginModel

class ShoppingLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingLoginModel
        fields = '__all__'