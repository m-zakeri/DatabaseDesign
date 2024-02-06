from django.contrib import admin

from django.utils.translation import gettext_lazy as _


class StatusFilter(admin.SimpleListFilter):
    title = _('ٔstatus')
    parameter_name = 'q'

    def lookups(self, request, model_admin):
        return (
            ('READ', _('Read')),
            ('UNREAD', _('Unread'))
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset

        return queryset.filter(status=self.value())
