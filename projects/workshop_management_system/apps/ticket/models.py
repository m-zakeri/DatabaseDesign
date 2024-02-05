from django.db import models
from apps.account.models import User
from apps.course.models import Course
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    status_ticket = (
        ('Read', _('read')),
        ('Unread', _('unread')),

    )
    priority_ticket = (('Many', _('MANY')),
                       ('Very Many', _('VERY MANY')),
                       ('Low', _('LOW')),
                       ('Very Low', _('VERY LOW')),)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket', verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ticket', null=True, blank=True,
                               verbose_name=_('Course'))
    subject = models.CharField(max_length=100, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))
    status = models.CharField(max_length=50, choices=status_ticket, default='Unread', verbose_name=_('Status'))
    priority = models.CharField(max_length=50, verbose_name=_('Priority'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subs',
                               verbose_name=_('Parent'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
