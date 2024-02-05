from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PaymentMethodFilter(admin.SimpleListFilter):
    title = 'payment method'
    parameter_name = 'q'

    def lookups(self, request, model_admin):
        return (
        ('Paid', _('PAID')),
        ('Unpaid', _('UNPAID')),
        ('Awaiting Payment', _('AWAITING PAYMENT'))

    )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(pament_method=self.value())
