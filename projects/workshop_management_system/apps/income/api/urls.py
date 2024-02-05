from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'teacher-income', views.TeacherIncomeViewSet, basename='teacher_income')

urlpatterns = [
    path('', include(router.urls))
]
