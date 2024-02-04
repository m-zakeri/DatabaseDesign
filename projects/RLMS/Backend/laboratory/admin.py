# Register your models here.
from django.contrib import admin
from .models import *
from .models import *

# Register your models here.
# admin.site.register(Student)


class StudentInline(admin.TabularInline):
    model = Student

    extra = 1


class SupervisortInline(admin.TabularInline):
    model = Supervisor
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [StudentInline, SupervisortInline]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    pass
