from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CartAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cart'
    verbose_name = _('cart')
