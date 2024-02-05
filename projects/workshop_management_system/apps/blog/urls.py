from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='list'),
    path('detail/<slug:slug>/', views.BlogDetailView.as_view(), name='detail')
]
