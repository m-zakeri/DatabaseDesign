from django.contrib import admin
from .models import TeacherIncome


@admin.register(TeacherIncome)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'amount', 'method', 'status')
    search_fields = ('teacher', 'course')
