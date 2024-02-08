from django.contrib import admin
from .models import Interview, Meeting, PersonelsMeeting


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("interviewer", "applier", "stage", "interview_date", "created")


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("establisher", "title", "start_date", "created")


@admin.register(PersonelsMeeting)
class PersonelsMeetingAdmin(admin.ModelAdmin):
    list_display = ("personel", "meeting", "created")
