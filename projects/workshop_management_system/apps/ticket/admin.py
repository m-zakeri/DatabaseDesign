from django.contrib import admin
from .models import Ticket
from .filter_admin import StatusFilter, PriorityFilter


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'subject', 'status', 'priority', 'is_publish')
    search_fields = ('user', 'course', 'subject')
    list_editable = ('is_publish',)
    list_filter = ('is_publish', StatusFilter, PriorityFilter)
