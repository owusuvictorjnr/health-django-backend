# from py_backend.users import serializers
from .models import Item, Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerialize):
    class Meta:
        model: Item
        fields = '__all__'