from django.urls import path
from .views import InterviewList, MeetingList, MeetingeStablisher, PersonelsMeetingList


urlpatterns = [
    path("", InterviewList.as_view(), name="interview-list"),
    path("list/", MeetingList.as_view(), name="meeting-list"),
    path("establisher/<str:username>/", MeetingeStablisher.as_view(), name="meeting-owner"),
    path("personels/", PersonelsMeetingList.as_view(), name="personels-meeting-list")
]
