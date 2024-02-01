from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import forms
from .models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    list_display = ["username", "email", "roles", "is_admin", "show_image"]
    list_filter = ["is_admin"]
    list_editable = ["is_admin"]
    prepopulated_fields = {'username': ('email',)}
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Personal info",
         {"fields": ["first_name", "last_name", "date_of_birth", "caption", "phone_number", "roles", "image"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "username",
                    "email",
                    "password1",
                    "password2"],
            },
        ),
    ]
    search_fields = ["email", "username"]
    ordering = ["email"]
    filter_horizontal = []


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_address', 'is_active']
    search_fields = ('user',)
    list_editable = ('is_active',)
    list_filter = ('is_active',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['user', 'platform', 'profile_link', 'is_active']
    search_fields = ('user', 'platform')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipient_name', 'card_number', 'is_active')
    search_fields = ('user', 'recipient_name')
    filter = ('is_active',)
    list_editable = ('is_active',)


admin.site.unregister(Group)
admin.site.register(NewUser)
admin.site.register(EmailChangePassword)
admin.site.register(Country)
admin.site.register(City)
