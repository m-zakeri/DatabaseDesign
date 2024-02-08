from django.contrib import admin
from .models import Personel, Position, Payroll, VacationRequest, PerformanceReview


@admin.register(Personel)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("user", "position", "created")


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "job_title", "created")


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ("personel", "salary", "reward", "pay_date", "created")


@admin.register(VacationRequest)
class VacationRequestAdmin(admin.ModelAdmin):
    list_display = (
        "personel",
        "request_date",
        "vacation_start",
        "vacation_end",
        "created",
    )


@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer", "personel", "score", "created")
