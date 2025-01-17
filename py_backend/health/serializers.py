from .models import HealthTip
from rest_framework import serializers


class healthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = '__all__'