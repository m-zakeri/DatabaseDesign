from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'customer-certificate', views.CertificateViewSet, basename='customer_certificate')

urlpatterns = [
    path('', include(router.urls))
]
