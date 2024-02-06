from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.account.models import User


class Notification(models.Model):
    status_notification = (
        ('READ', _('Read')),
        ('UNREAD', _('Unread'))
    )
    user = models.ManyToManyField(User, related_name='notification', verbose_name=_('User'))
    subject = models.CharField(max_length=100, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))
    status = models.CharField(max_length=50, choices=status_notification, verbose_name=_('Status'))
    display = models.BooleanField(default=False, verbose_name=_('Is Display'))
    type = models.CharField(max_length=50, verbose_name=_('Type'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
