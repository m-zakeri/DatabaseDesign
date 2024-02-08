from rest_framework import serializers
from .models import Resume, Degree, Skill, Experinece


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ("degree", "institute", "field")


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("title", "description")


class ExperineceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experinece
        fields = ("position", "company_name", "years_of_experience")


class ResumeSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source="user.username")
    degrees = DegreeSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    experiences = ExperineceSerializer(many=True, read_only=True)
    created = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = ("user", "degrees", "skills", "experiences", "created")

    def get_created(self, obj):
        return obj.created.date()    
