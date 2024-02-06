from rest_framework import serializers
from apps.customer import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerCertificate
        fields = '__all__'
