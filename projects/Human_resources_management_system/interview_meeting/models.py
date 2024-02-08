from django.db import models
from personels.models import Personel
from users.models import User


class Interview(models.Model):
    
    interviewer = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="interviews")
    applier = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviews")
    stage = models.PositiveSmallIntegerField(default=0)
    interview_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "interview"
        verbose_name_plural = "interviews"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"inte:{self.interviewer} - appl:{self.applier}"


class Meeting(models.Model):

    establisher = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="meeting_owner")
    title = models.CharField(max_length=45, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "meeting"
        verbose_name_plural = "meetings"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.title}"
    

class PersonelsMeeting(models.Model):

    personel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="has_meetings")
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="personels_meeting")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "personel meeting"
        verbose_name_plural = "personels meeting"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.personel} - {self.meeting}"
    