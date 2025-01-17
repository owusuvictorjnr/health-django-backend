from .models import Item, Category
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model: Item
        fields = '__all__'