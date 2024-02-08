from rest_framework import serializers
from .models import Interview, Meeting, PersonelsMeeting


class InterviewSerializer(serializers.ModelSerializer):

    interviewer = serializers.CharField(source="interviewer.user.username")
    applier = serializers.CharField(source="applier.username")
    created = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        fields = ("interviewer", "applier", "stage", "interview_date", "created")

    def get_created(self, obj):
        return obj.created.date()     
    

class MeetingSerializer(serializers.ModelSerializer):

    establisher = serializers.CharField(source="establisher.user.username")
    created = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = ("establisher", "title", "description", "start_date", "created")  

    def get_created(self, obj):
        return obj.created.date()   
      

class PersonelsMeetingSerializer(serializers.ModelSerializer):

    personel = serializers.CharField(source="personel.user.username")
    meeting = MeetingSerializer()
    created = serializers.SerializerMethodField()

    class Meta:
        model = PersonelsMeeting
        fields = ("personel", "meeting", "created")
        
    def get_created(self, obj):
        return obj.created.date()
    