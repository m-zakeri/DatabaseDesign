from django.urls import URLPattern, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("pages/dashboard/", views.dashboard, name="dashboard"),
]
