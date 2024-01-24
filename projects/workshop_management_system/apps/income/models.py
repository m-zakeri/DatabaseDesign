from django.db import models
from apps.course.models import Course
from apps.teacher.models import Teacher
from django.utils.translation import gettext_lazy as _


class TeacherIncome(models.Model):
    status_income = (
        ('Paid', _('Paid')),
        ('Awaiting Payment', _('Awaiting Payment')),
        ('Unpaid', _('Unpaid'))
    )
    method_income = (
        ('Online', _('Online')),
        ('Card by card', _('Card by card'))

    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='income', verbose_name=_('Teacher'))
    course = models.ManyToManyField(Course, related_name='teacher_income', verbose_name=_('Course'))
    amount = models.PositiveIntegerField(verbose_name=_('Amount'))
    status = models.CharField(max_length=50, choices=status_income, default='Unpaid', verbose_name=_('Status'))
    method = models.CharField(max_length=50,choices=method_income,default='Online', verbose_name=_('Method'))
    payment_date = models.DateTimeField(verbose_name=_('Payment Date'))
    tax_amount = models.PositiveIntegerField(verbose_name=_('Tax Amount'))
    transaction_image = models.FileField(upload_to='document/transaction/income_teacher',
                                         verbose_name=_('Transaction Image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')
