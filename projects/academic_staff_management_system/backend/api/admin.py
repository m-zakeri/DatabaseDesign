from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin

from . import models


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Person)
admin.site.register(models.Professor)
admin.site.register(models.PhoneNumber)
admin.site.register(models.Address)
admin.site.register(models.Building)
admin.site.register(models.Department)
admin.site.register(models.Education)
admin.site.register(models.Employee)
admin.site.register(models.Faculty)
admin.site.register(models.Field)
