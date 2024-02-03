from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'city', views.CityViewSet, basename='city')
router.register(r'country', views.CountryViewSet, basename='country')
router.register(r'address', views.AddressViewSet, basename='address')
router.register(r'social-media', views.SocialMediaViewSet, basename='social_media')
router.register(r'card', views.CardViewSet, basename='card')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += router.urls
