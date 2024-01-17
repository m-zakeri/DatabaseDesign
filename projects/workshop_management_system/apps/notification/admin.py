from django.contrib import admin
from .models import *
from .filter_admin import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'subject', 'display')
    search_fields = ('subject',)
    list_editable = ('display',)
    list_filter = ('display', StatusFilter)
