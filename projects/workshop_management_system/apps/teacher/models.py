from django.db import models
from apps.account.models import User
from .validators import validate_credit_work_phone

from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    gender_teacher = (
        ('man', _('MAN')),
        ('woman', _('WOMAN'))
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher', verbose_name=_('User'))
    description = models.TextField(verbose_name=_('Description'))
    score = models.FloatField(default=0,verbose_name=_('Score'))
    gender = models.CharField(max_length=50, choices=gender_teacher, default='man', verbose_name=_('Gender'))
    is_valid = models.BooleanField(default=False, verbose_name=_('Is Valid'))
    crated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')


class Work(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='work', verbose_name=_('Teacher'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    work_phone = models.CharField(max_length=11, validators=[validate_credit_work_phone], verbose_name=_('Work Phone'))
    employment_file = models.FileField(upload_to='document/certificate/work', verbose_name=_('Employment Photo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Work')
        verbose_name_plural = _('Works')


class Skill(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='skill', verbose_name=_('Teacher'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    certificate_photo = models.FileField(upload_to='document/certificate/skill', verbose_name=_('Certificate Photo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.teacher} -> {self.name}'

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')


class LevelEducation(models.Model):
    graduations = (
        ("diploma", _("DIPLOMA")),
        ("Bachelor's degree", _("BACHELOR'S DEGREE")),
        ("Master's degree", _("MASTER'S DEGREE ")),
        ("doctorate degree", _("DOCTORATE DEGREE"))

    )

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='level_education',
                                verbose_name=_('Teacher'))
    name_university = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Name University'))
    date_of_graduation = models.DateField(verbose_name=_('Date Of Graduation'))
    graduation = models.CharField(max_length=50, choices=graduations, default='diploma', verbose_name=_('Graduation'))
    Academic_discipline = models.CharField(max_length=50, verbose_name=_('Academic Discipline'))
    graduation_image = models.FileField(upload_to='file/certificate/graduation_teacher',
                                        verbose_name=_('graduation image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Level Of Education')
        verbose_name_plural = _('Levels Of Education')
