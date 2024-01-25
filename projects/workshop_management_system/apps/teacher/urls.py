from django.urls import path
from . import views

app_name = 'teacher_app'
urlpatterns = [
    path('list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail')
]
