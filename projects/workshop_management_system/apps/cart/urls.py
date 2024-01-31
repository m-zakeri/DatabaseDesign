from django.urls import path
from . import views

app_name = 'cart_app'
urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('remove/course/<slug:slug>/', views.RemoveCourseView.as_view(), name='remove_course'),
    path('order/creation/', views.OrderCreationView.as_view(), name='order_creation'),
    path('order/detail/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/coupon/<int:id>/', views.CouponView.as_view(), name='coupon')
]
