from django.db import models
from apps.customer.models import Customer
from apps.course.models import Course
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order', verbose_name=_('Customer'))
    total_price = models.CharField(max_length=50, verbose_name=_('Total price'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid'))
    is_discount = models.BooleanField(default=False, verbose_name=_('Is Discount'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.customer} -> {self.total_price}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('ORDER'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='order_item', verbose_name=_('COURSE'))
    final_price = models.PositiveIntegerField(verbose_name=_('FINAL PRICE'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('CREATED AT'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('UPDATED AT'))

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
