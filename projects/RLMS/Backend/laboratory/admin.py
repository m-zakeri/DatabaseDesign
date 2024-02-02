from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'age']

@admin.register(Email)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['person_id', 'email_address', 'email_type']

@admin.register(Phone)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['person_id', 'phone_number']

@admin.register(Student)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['person_id', 'field', 'gpa', 'university', 'educational_degree']

@admin.register(Subscription_plan)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'start_date', 'subscription_duration', 'price', 'end_date']

@admin.register(Course)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'name', 'subject', 'platform']

@admin.register(Teammates)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["Teammates"]
