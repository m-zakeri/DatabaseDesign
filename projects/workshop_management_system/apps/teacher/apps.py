from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TeacherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.teacher'
    verbose_name = _('teacher')
