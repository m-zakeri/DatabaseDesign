from django.urls import path
from . import views

app_name = 'contact_app'
urlpatterns = [
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path('about-us/',views.AboutUsView.as_view(),name='about_us')
]
