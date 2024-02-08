from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, WasEmployeed, PhoneNumber, Address
from .forms import UserAdminCreationForm


class UserAdmin(BaseUserAdmin):

    list_display = ("username", "first_name", "last_name", "birth_date", "gender", "created")
    list_filter = ("gender",)


    add_form = UserAdminCreationForm

    fieldsets = [
        (None, {"fields": ["username", "first_name", "last_name", "birth_date", "gender", "password"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser"]}),
    ]
   
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "first_name", "last_name", "birth_date", "gender", "password1", "password2"],
            },
        ),
    ]

    ordering = ["created"]


admin.site.register(User, UserAdmin)


@admin.register(WasEmployeed)
class WasEmployeedAdmin(admin.ModelAdmin):
    list_display = ("user", "employed_date", "dismissal_date", "created")


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("user", "main_number", "home_number", "second_number", "created")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "zone", "created")
            