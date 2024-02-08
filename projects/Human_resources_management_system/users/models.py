from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    MALE = "M"
    FEMALE = "F"

    GENDER_CHOICES = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
    )

    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, editable=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        indexes = [models.Index(fields=["username" ,"first_name", "last_name"])]
        ordering = ["created"]

    def __str__(self) -> str:
        return f"{self.username} - user"
    

class WasEmployeed(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="was_employeed")
    employed_date = models.DateField(null=True, blank=True)
    dismissal_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "was employeed"
        verbose_name_plural = "was employeeds"
        
    def __str__(self) -> str:
        return f"{self.user} wasemployeed"


class PhoneNumber(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="phone_numbers")
    main_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    home_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    second_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "phone number"
        verbose_name_plural = "phone numbers"
        indexes = [models.Index(fields=["main_number" ,"home_number", "second_number"])]

    def __str__(self) -> str:
        return f"{self.user} {self.main_number}"
    

class Address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    country = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zone = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"
        indexes = [models.Index(fields=["country" ,"city", "zone"])]

    def __str__(self) -> str:
        return f"{self.user} {self.country}"