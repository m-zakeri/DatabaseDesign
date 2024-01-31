from django.urls import path
from . import views

app_name = 'cart_app'
urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('remove/course/<slug:slug>/', views.RemoveCourseView.as_view(), name='remove_course')
]
