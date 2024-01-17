from django.db import models
from apps.account.models import User
from apps.course.models import Course
from apps.teacher.models import Teacher
from django.utils.translation import gettext_lazy as _
from apps.account.validators import validate_credit_card_number


class Transaction(models.Model):
    currencies = (
        ('Rial', _('Rial')),
        ('Dollar', _('Dollar')),
    )
    status_transaction = (
        ('Paid', _('PAID')),
        ('Unpaid', _('UNPAID')),
        ('Awaiting Payment', _('AWAITING PAYMENT'))

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction', verbose_name=_('User'))
    course = models.ManyToManyField(Course, related_name='transaction', verbose_name=_('Course'))
    teacher = models.ManyToManyField(Teacher, related_name='transaction', verbose_name=_('Teacher'))
    amount = models.PositiveIntegerField(verbose_name=_('Amount'))
    currency = models.CharField(max_length=50, choices=currencies, default='Rial', verbose_name=_('Currency'))
    payment_method = models.CharField(max_length=50, verbose_name=_('Payment Method'))
    status = models.CharField(max_length=50, choices=status_transaction, default='Unpaid', verbose_name=_('Status'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    sender_card_number = models.CharField(max_length=11, validators=[validate_credit_card_number],
                                          verbose_name=_("Sender's Card Number"))
    recipient_card_number = models.CharField(max_length=11, validators=[validate_credit_card_number],
                                             verbose_name=_("Recipient's Card Number"))
    transaction_image = models.FileField(upload_to='document/transaction/user', verbose_name=_('Transaction Image'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
