from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_list_or_404
from .models import Interview, Meeting, PersonelsMeeting
from .serializers import InterviewSerializer, MeetingSerializer, PersonelsMeetingSerializer
from utils import CustomPagination


class InterviewList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = InterviewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        interviews = Interview.objects.select_related("interviewer", "applier").all()
        return interviews
    

class MeetingList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = MeetingSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        meetings = Meeting.objects.select_related("establisher").all()
        return meetings


class MeetingeStablisher(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = MeetingSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        personel_meetings = get_list_or_404(Meeting, establisher__user__username=self.kwargs["username"])
        return personel_meetings


class PersonelsMeetingList(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = PersonelsMeetingSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        meeting_personels = PersonelsMeeting.objects.select_related("meeting", "personel").all()
        return meeting_personels
    