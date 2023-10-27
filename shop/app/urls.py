from django.urls import path, include
from .views import ProductListView, OrderCreateView, PaymentCreateView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('orders/create/', OrderCreateView.as_view(), name='create-order'),
    path('payments/create/', PaymentCreateView.as_view(), name='create-payment'),
]
