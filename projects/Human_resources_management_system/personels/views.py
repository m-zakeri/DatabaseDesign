from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Personel, VacationRequest, Payroll, PerformanceReview
from .serializers import (PersonelSerializer, VacationRequestSerializer,
                           PayrollSerializer, PerformanceReviewSerializer)
from utils import CustomPagination


class PersonelList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = PersonelSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        personels = Personel.objects.select_related("position").all()
        return personels


class PersonelDetail(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, username):

        personel = get_object_or_404(Personel, user__username=username)
        serilizer = PersonelSerializer(personel)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class VacationRequestList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = VacationRequestSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        vacation_requests = VacationRequest.objects.select_related("personel").all()
        return vacation_requests


class PayrollList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = PayrollSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        payrolls = Payroll.objects.select_related("personel").all()
        return payrolls
    

class PerformanceReviewList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = PerformanceReviewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        performance_reviews = PerformanceReview.objects.select_related("personel").all()
        return performance_reviews