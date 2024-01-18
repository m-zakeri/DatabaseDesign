from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'account_app'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]
