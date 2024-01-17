from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class StatusFilter(admin.SimpleListFilter):
    title = 'status'
    parameter_name = 'q'

    def lookups(self, request, model_admin):
        return (
            ('Read', _('READ')),
            ('Unread', _('UNREAD')),

        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(status=self.value())


class PriorityFilter(admin.SimpleListFilter):
    title = 'priority'
    parameter_name = 'name_priority'

    def lookups(self, request, model_admin):
        return (('Many', _('MANY')),
                ('Very Many', _('VERY MANY')),
                ('Low', _('LOW')),
                ('Very Low', _('VERY LOW')),)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(priority=self.value())
