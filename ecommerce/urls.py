
from django.urls import path
from .views import ProductList, OrderList, api_root

urlpatterns = [
    path('', api_root),
    path('products/', ProductList.as_view(), name='product-list'),
    path('orders/', OrderList.as_view(), name='order-list'),
]
