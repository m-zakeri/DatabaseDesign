from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='list')
]
