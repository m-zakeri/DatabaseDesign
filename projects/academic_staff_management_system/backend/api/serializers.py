from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        ]


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Education
        fields = "__all__"


class PhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = "__all__"


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Building
        fields = "__all__"


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Faculty
        fields = "__all__"


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Office
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Field
        fields = "__all__"


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Professor
        fields = "__all__"


class ResearcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Researcher
        fields = "__all__"


class ResearchMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ResearchMember
        fields = "__all__"


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Schedule
        fields = "__all__"


class LaboratorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Laboratory
        fields = "__all__"


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Library
        fields = "__all__"

class DepartmentResponibilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DepartmentResponibility
        fields = "__all__"
