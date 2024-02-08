from django.urls import path
from .views import CourseList, PersonelCourseList


urlpatterns = [
    path("", CourseList.as_view(), name="course-list"),
    path("personel/", PersonelCourseList.as_view(), name="personel-courses")
]