from rest_framework import serializers
from apps.blog import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogCategory
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogLabel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogDescription
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogComment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikesBlogComment
        fields = '__all__'
