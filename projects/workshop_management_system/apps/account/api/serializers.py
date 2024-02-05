from rest_framework import serializers
from apps.account import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = models.Address
        fields = '__all__'
        extra_kwargs = {
            'country': {'required': True},
            'city': {'required': True}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return models.Address.objects.create(**validated_data)


class SocialMediaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = models.SocialMedia
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return models.SocialMedia.objects.create(**validated_data)


class CardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = models.Card
        fields = '__all__'
        write_only_field = ('user',)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return models.Card.objects.create(**validated_data)
