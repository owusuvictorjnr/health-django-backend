from django.urls import path
from .views import HealthTipListView, HealthTipDetailView


urlpatterns = [
    path('', HealthTipListView.as_view(), name='health-tip-list'),
    path('<int:pk>/', HealthTipDetailView.as_view(), name='health-tip-detail')
    
]

