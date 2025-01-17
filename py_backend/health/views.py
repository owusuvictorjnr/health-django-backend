from django.shortcuts import render
from rest_framework import generics
from .models import HealthTip
from .serializers import healthTipSerializer

# Create your views here.
class HealthTipList(generics.ListCreateAPIView):
    queryset = HealthTip.objects.all()
    serializer_class = healthTipSerializer
    
    
class HealthTipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthTip.objects.all()
    serializer_class = healthTipSerializer