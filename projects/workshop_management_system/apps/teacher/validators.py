from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_credit_work_phone(value):
    if not (value.isdigit() and len(value) == 8):
        raise ValidationError(_('Invalid credit work phone.'))
