from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register(r'order', views.OrderViewSet, basename='order'),
router.register(r'order-item', views.OrderItemViewSet, basename='order_item'),

urlpatterns = [
    path('', include(router.urls))
]
