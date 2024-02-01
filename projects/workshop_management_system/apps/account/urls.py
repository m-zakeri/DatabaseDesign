from django.urls import path
from . import views

app_name = 'account_app'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/email/', views.VerifyEmail.as_view(), name='verify_email'),
    path('password/forgot/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('password/change/<str:token>/', views.ChangePasswordView.as_view(), name='change_password'),
    path('add/address/', views.AddAddressView.as_view(), name='add_address')
]
