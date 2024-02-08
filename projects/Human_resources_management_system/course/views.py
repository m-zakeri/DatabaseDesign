from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from .models import Course, PersonelCourse
from .serializers import CourseSerializer, PersonelCourseSerializer
from utils import CustomPagination


class CourseList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        courses = Course.objects.select_related("instructor", "building").all()
        return courses


class PersonelCourseList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = PersonelCourseSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        personel_courses = PersonelCourse.objects.select_related("course", "personel").all()
        return personel_courses