from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class LevelFilter(admin.SimpleListFilter):
    title = 'level'
    parameter_name = 'q'

    def lookups(self, request, model_admin):
        return (
            ('All levels', _('All levels')),
            ('Beginner', _('Beginner')),
            ('Preliminary', _('Preliminary')),
            ('Advanced', _('Advanced')),

        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(level=self.value())


class StateFilter(admin.SimpleListFilter):
    title = 'state'
    parameter_name = 'q'

    def lookups(self, request, model_admin):
        return (
            ('Start of the course', _('Start of the course')),
            ('Uploading', _('Uploading')),
            ('Completion of the course', _('Completion of the course'))

        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(state=self.value())
