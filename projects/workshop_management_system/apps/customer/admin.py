from django.contrib import admin
from .models import *


class CertificateAdmin(admin.StackedInline):
    model = CustomerCertificate


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = (CertificateAdmin,)


@admin.register(CustomerCertificate)
class CustomerCertificateAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'type')
    search_fields = ('customer',)
