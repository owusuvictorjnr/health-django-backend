from django.shortcuts import render
from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

# Create your views here.
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer