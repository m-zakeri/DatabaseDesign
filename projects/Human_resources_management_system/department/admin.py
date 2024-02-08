from django.contrib import admin
from .models import Department, Building, BuildingDepartment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("director", "name", "created")


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("city", "zone", "created")


@admin.register(BuildingDepartment)
class BuildingDepartmentAdmin(admin.ModelAdmin):
    list_display = ("building", "department", "created")
