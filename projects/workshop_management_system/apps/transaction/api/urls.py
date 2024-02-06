from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'transaction', views.TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls))
]
