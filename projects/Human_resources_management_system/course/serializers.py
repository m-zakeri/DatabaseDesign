from rest_framework import serializers
from department.serializers import BuildingSerializer
from .models import Course, PersonelCourse


class CourseSerializer(serializers.ModelSerializer):

    instructor = serializers.CharField(source="instructor.user.username")
    building = BuildingSerializer()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("instructor", "building", "title",
                   "description", "start_date", "end_date", "created")

    def get_created(self, obj):
        return obj.created.date()
    

class PersonelCourseSerializer(serializers.ModelSerializer):

    personel = serializers.CharField(source="personel.user.username")
    course = CourseSerializer()
    created = serializers.SerializerMethodField()

    class Meta:
        model = PersonelCourse
        fields = ("personel", "course", "score", "created")

    def get_created(self, obj):
        return obj.created.date()
    