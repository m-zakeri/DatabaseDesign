from rest_framework import serializers
from users.models import User
from .models import Personel, Position, VacationRequest, Payroll, PerformanceReview


class UserPersonelSerializer(serializers.ModelSerializer):

    created = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "birth_date", "gender", "created")

    def get_created(self, obj):
        return obj.created.date()

    def get_gender(self, obj):
        return obj.get_gender_display()


class PositoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("name", "job_title")


class PersonelSerializer(serializers.ModelSerializer):

    user = UserPersonelSerializer(read_only=True)
    position = PositoinSerializer(read_only=True)
    created = serializers.SerializerMethodField()

    class Meta:
        model = Personel
        fields = ("user", "position", "created")

    def get_created(self, obj):
        return obj.created.date()
    

class VacationRequestSerializer(serializers.ModelSerializer):

    personel = serializers.CharField(source="personel.user.username")
    created = serializers.SerializerMethodField()

    class Meta:
        model = VacationRequest
        fields = ("personel", "description", "request_date",
                   "vacation_start", "vacation_end", "created")    
        
    def get_created(self, obj):
        return obj.created.date()    
    

class PayrollSerializer(serializers.ModelSerializer):

    personel = serializers.CharField(source="personel.user.username")
    pay_date = serializers.SerializerMethodField() 
    created = serializers.SerializerMethodField()

    class Meta:
        model = Payroll
        fields = ("personel", "salary", "reward", "pay_date", "created")

    def get_pay_date(self, obj):
        return obj.pay_date.date()

    def get_created(self, obj):
        return obj.created.date()
    

class PerformanceReviewSerializer(serializers.ModelSerializer):

    reviewer = serializers.CharField(source="reviewer.user.username")
    personel = serializers.CharField(source="personel.user.username")
    created = serializers.SerializerMethodField()

    class Meta:
        model = PerformanceReview
        fields = ("reviewer", "personel", "description", "score", "created")

    def get_created(self, obj):
        return obj.created.date() 
