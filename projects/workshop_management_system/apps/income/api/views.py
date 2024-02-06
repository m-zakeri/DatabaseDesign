from rest_framework.viewsets import ModelViewSet
from apps.income import models
from . import serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TeacherIncomeViewSet(ModelViewSet):
    queryset = models.TeacherIncome.objects.all()
    serializer_class = serializers.TeacherIncomeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
