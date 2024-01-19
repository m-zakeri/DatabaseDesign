from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:id>/', views.LikeCoureseView.as_view(), name='like_course')
]
