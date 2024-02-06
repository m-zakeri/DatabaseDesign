from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'teacher', views.TeacherViewSet, basename='teacher')
router.register(r'teacher-work', views.WorkViewSet, basename='teacher_work')
router.register(r'teacher-skill', views.SkillViewSet, basename='teacher_skill')
router.register(r'teacher-level-education', views.LevelEducationViewSet, basename='teacher_level_education')

urlpatterns = [
    path('', include(router.urls))
]
