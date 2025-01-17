from .models import HealthTip


class healthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = '__all__'