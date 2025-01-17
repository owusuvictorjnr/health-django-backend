from django.shortcuts import render
from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer

# Create your views here.
class CartItemViewList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    
class CartItemViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer