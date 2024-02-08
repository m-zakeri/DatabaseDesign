from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from utils import CustomPagination


class UserList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        users = User.objects.prefetch_related("was_employeed", "addresses", "phone_numbers").all()
        return users


class UserDetail(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, username):
        print("salam")
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    