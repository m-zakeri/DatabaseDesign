from rest_framework import serializers
from apps.teacher import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Work
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'


class LevelEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LevelEducation
        fields = '__all__'
