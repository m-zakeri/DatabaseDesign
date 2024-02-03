from rest_framework.viewsets import ModelViewSet
from apps.teacher import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser


class TeacherViewSet(ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class WorkViewSet(ModelViewSet):
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class SkillViewSet(ModelViewSet):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class LevelEducationViewSet(ModelViewSet):
    queryset = models.LevelEducation.objects.all()
    serializer_class = serializers.LevelEducationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
