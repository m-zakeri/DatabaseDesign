from rest_framework import serializers
from apps.income import models


class TeacherIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherIncome
        fields = '__all__'
        extra_kwargs = {
            'status': {'required': True},
            'method': {'required': True}

        }
