from rest_framework import serializers
from .models import User, WasEmployeed, Address, PhoneNumber


class WasEmployeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasEmployeed
        fields = ("employed_date", "dismissal_date", "description")


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ("main_number", "home_number", "second_number")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("country", "city", "address", "zone")


class UserSerializer(serializers.ModelSerializer):

    was_employeed = WasEmployeedSerializer(many=True, read_only=True)
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)
    gender = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "birth_date", "gender",
                   "created", "was_employeed", "phone_numbers", "addresses")

    def get_created(self, obj):
        return obj.created.date()

    def get_gender(self, obj):
        return obj.get_gender_display()
    