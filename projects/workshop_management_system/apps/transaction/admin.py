from .models import Transaction
from .filter_admin import *


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_method', 'status')
    search_fields = ('user', 'course')
    list_filter = ('status', PaymentMethodFilter)
    list_editable = ('status',)
