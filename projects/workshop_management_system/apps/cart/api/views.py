from rest_framework.viewsets import ModelViewSet

from apps.cart import models
from . import serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OrderViewSet(ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class OrderItemViewSet(ModelViewSet):
    queryset = models.OrderItem
    serializer_class = serializers.OrderItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
