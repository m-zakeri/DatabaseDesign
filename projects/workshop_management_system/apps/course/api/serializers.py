from rest_framework import serializers
from apps.course import models


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseLabel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDescription
        fields = '__all__'


class CourseLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseLikes
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCertificate
        fields = '__all__'


class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CouponCode
        fields = '__all__'


class LikesCourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikesCourseComment
        fields = '__all__'


class FAQFrequentlySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQFrequently
        fields = '__all__'


class AskedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AskedQuestion
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Season
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meeting
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exam
        fields = '__all__'


class ExamScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamScore
        fields = '__all__'


class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Festival
        fields = '__all__'


class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseComment
        fields = '__all__'
