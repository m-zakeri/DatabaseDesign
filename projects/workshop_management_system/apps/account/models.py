from django.db import models
from .validators import *
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.html import format_html

from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError(_("Users must have an username"))

        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    role_user = (
        ('COSTUMER', _('Costumer')),
        ('TEACHER', _('Teacher')),
        ('TEACHER AND COSTUMER', _('Teacher and Costumer'))
    )

    username = models.CharField(max_length=50, unique=True, verbose_name=_('Username'))
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Last Name'))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_('Date Of Birth'))
    image = models.ImageField(default='/image/user/user.png', upload_to='image/user', verbose_name=_('image'))

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_('Email Address')

    )
    phone_number = models.CharField(max_length=11, null=True, blank=True, validators=[validate_credit_phone_number],
                                    verbose_name=_('Phone Number'))
    caption = models.CharField(max_length=300, null=True, blank=True, verbose_name=_('Caption'))

    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Is Admin'))
    roles = models.CharField(max_length=50, choices=role_user, default='COSTUMER', verbose_name=_('Roles'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def show_image(self):
        return format_html(f"<img src={self.image.url} width='50px' height='50px'>")

    show_image.short_description = _('image')

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address', verbose_name=_('User'))
    country = models.CharField(max_length=50, default=_('Iran'), verbose_name=_('Country'))
    city = models.CharField(max_length=50, verbose_name=_('City'))
    state = models.CharField(max_length=50, verbose_name=_('State'))
    postal_code = models.CharField(max_length=10, verbose_name=_('Postal Code'))
    full_address = models.TextField(verbose_name=_('Full Address'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f"{self.user} -> {self.full_address}"

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media', verbose_name=_('User'))
    platform = models.CharField(max_length=50, verbose_name=_('Social Media Name'))
    profile_link = models.URLField(max_length=200, verbose_name=_('Link'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.user} -> {self.profile_link}'

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card', verbose_name=_('User'))
    card_number = models.CharField(max_length=16, unique=True, validators=[validate_credit_card_number],
                                   verbose_name=_('Card Number'))
    cv2 = models.CharField(max_length=4, validators=[validate_credit_cv2], verbose_name=_('Card Security Code'))
    date_month = models.CharField(max_length=2, verbose_name=_('Card Expiration Month'))
    date_year = models.CharField(max_length=2, verbose_name=_('Card Expiration Year'))
    recipient_name = models.CharField(max_length=50, verbose_name=_('Recipient Name'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.recipient_name} -> {self.card_number}'

    class Meta:
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')


class NewUser(models.Model):
    token = models.CharField(max_length=300)
    randcode = models.CharField(max_length=5)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class EmailChangePassword(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
