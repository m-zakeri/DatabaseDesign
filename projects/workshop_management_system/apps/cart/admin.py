from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'is_paid', 'is_discount')
    search_fields = ('customer',)
    list_filter = ('is_paid', 'is_discount')
    list_editable = ('is_paid', 'is_discount')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('course', 'final_price')
