from django.urls import path
from . import views

app_name = 'course_app'
urlpatterns = [
    path('list/', views.CourseListView.as_view(), name='course_list'),
    path('like/<int:id>/', views.LikeCoureseView.as_view(), name='like_course')

]
