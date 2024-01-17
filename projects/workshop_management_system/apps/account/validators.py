from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_credit_phone_number(value):
    if not (value.isdigit() and len(value) == 11):
        raise ValidationError(_('Invalid credit phone number.'))


def validate_credit_card_number(value):
    if not (value.isdigit() and len(value) == 16):
        raise ValidationError(_('Invalid credit card number.'))


def validate_credit_cv2(value):
    if not (value.isdigit() and (len(value) == 4 or len(value) == 3)):
        raise ValidationError(_('Invalid credit cv2.'))
