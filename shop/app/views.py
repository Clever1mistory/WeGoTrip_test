from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics

from .serializers import ProductSerializer, OrderSerializer, PaymentSerializer
from .models import Product


@swagger_auto_schema()
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@swagger_auto_schema()
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


@swagger_auto_schema()
class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer