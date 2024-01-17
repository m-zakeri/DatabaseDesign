from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class GenderFilter(admin.SimpleListFilter):
    title = 'ٔgender'
    parameter_name = 'q'

    def lookups(self, request, model_admin):
        return (
            ('man', _('MAN')),
            ('woman', _('WOMAN'))
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset

        return queryset.filter(gender=self.value())
