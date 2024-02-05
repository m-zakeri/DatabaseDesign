from django.urls import path
from . import views

app_name = 'teacher_app'
urlpatterns = [
    path('list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('add/stage/first/', views.FirstStageAdmissionView.as_view(), name='first_stage_admission'),
    path('add/stage/second/', views.SecondStageAdmission.as_view(), name='second_stage_admission'),
    path('add/stage/third/', views.ThirdStageAdmission.as_view(), name='third_stage_admission'),
    path('add/stage/fourth/', views.FourthStageAdmission.as_view(), name='Fourth_stage_admission'),
    path('add/stage/fifth/', views.FifthStageAdmissionView.as_view(), name='fifth_stage_admission'),
    path('add/stage/sixth/', views.SixthStageAdmissionView.as_view(), name='sixth_stage_admission'),
    path('add/', views.TeacherAddedView.as_view(), name='teacher_add')
]
