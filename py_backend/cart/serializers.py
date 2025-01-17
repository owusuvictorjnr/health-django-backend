from .models import CartItem


class CartItemSerializer(serializers.ModelSerilazer):
    class Meta:
        model = CartItem
        fields = '__all__'