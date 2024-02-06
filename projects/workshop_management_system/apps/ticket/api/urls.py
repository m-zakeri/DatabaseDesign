from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'ticket', views.TicketViewSet, basename='ticket')


urlpatterns = [
    path('', include(router.urls))
]