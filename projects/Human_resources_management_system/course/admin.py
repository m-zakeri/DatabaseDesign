from django.contrib import admin
from .models import Course, PersonelCourse


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("instructor", "building", "title", "start_date", "end_date", "created")


@admin.register(PersonelCourse)
class PersonelCourseAdmin(admin.ModelAdmin):
    list_display = ("personel", "course", "score", "created")