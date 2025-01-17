from django.urls import path
from .views import CartItemViewList, CartItemViewDetail


urlpatterns = [
    path('items/', CartItemViewList.as_view(), name='cart-item-list'),
    path('items/<int:pk>/', CartItemViewDetail.as_view(), name='cart-item-detail')
]
