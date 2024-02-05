from django.db import models
from apps.account.models import User
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', verbose_name=_('User'))
    is_valid = models.BooleanField(default=True, verbose_name=_('Is valid'))

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


class CustomerCertificate(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_certificate',
                                 verbose_name=_('Customer'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    type = models.CharField(max_length=50, verbose_name=_('Type'))
    certificate_image = models.FileField(upload_to='documents/certificate/customer',
                                         verbose_name=_('Certificate Image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Graduation')
        verbose_name_plural = _('Graduations')
