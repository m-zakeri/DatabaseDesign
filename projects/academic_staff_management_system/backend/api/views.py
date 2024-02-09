from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from . import serializers
from . import models
from . import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.UserFilter


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.PersonFilter


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.AddressFilter


class EducationViewSet(viewsets.ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.EducationFilter


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = models.PhoneNumber.objects.all()
    serializer_class = serializers.PhoneNumberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.PhoneNumberFilter


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.BuildingFilter


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.FacultyFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.DepartmentFilter


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.OfficeFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.EmployeeFilter


class FieldViewSet(viewsets.ModelViewSet):
    queryset = models.Field.objects.all()
    serializer_class = serializers.FieldSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.FieldFilter


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = models.Professor.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.ProfessorFilter


class ResearcherViewSet(viewsets.ModelViewSet):
    queryset = models.Researcher.objects.all()
    serializer_class = serializers.ResearcherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.ResearcherFilter


class ResearchViewSet(viewsets.ModelViewSet):
    queryset = models.Research.objects.all()
    serializer_class = serializers.ResearcherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.ResearchFilter


class ResearchMemberViewSet(viewsets.ModelViewSet):
    queryset = models.ResearchMember.objects.all()
    serializer_class = serializers.ResearchMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.ResearchMemberFilter


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.ScheduleFilter


class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = models.Laboratory.objects.all()
    serializer_class = serializers.LaboratorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.LaboratoryFilter


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.LibraryFilter


class DepartmentResponibility(viewsets.ModelViewSet):
    queryset = models.DepartmentResponibility.objects.all()
    serializer_class = serializers.DepartmentResponibilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    