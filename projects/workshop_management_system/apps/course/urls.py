from django.urls import path
from . import views

app_name = 'course_app'
urlpatterns = [
    path('list/', views.CourseListView.as_view(), name='course_list'),
    path('detail/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('like/<int:id>/', views.LikeCourseView.as_view(), name='like_course'),
    path('like/comment/<int:id>/', views.LikeCourseCommentView.as_view(), name='like_comment'),


]
