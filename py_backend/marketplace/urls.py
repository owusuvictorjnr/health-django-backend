from django.urls import path
from .views import CategoryListView, ItemDetailView, ItemListView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail')
]
