from rest_framework.viewsets import ModelViewSet
from . import serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.course import models


class LanguageViewSet(ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class LabelViewSet(ModelViewSet):
    queryset = models.CourseLabel.objects.all()
    serializer_class = serializers.LabelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CategoryViewSet(ModelViewSet):
    queryset = models.CourseCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CourseViewSet(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class DescriptionViewSet(ModelViewSet):
    queryset = models.CourseDescription.objects.all()
    serializer_class = serializers.DescriptionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CourseLikeViewSet(ModelViewSet):
    queryset = models.CourseLikes.objects.all()
    serializer_class = serializers.CourseLikesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CertificateViewSet(ModelViewSet):
    queryset = models.CourseCertificate.objects.all()
    serializer_class = serializers.CertificateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CouponCodeViewSet(ModelViewSet):
    queryset = models.CouponCode.objects.all()
    serializer_class = serializers.CouponCodeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class LikesCourseCommentViewSet(ModelViewSet):
    queryset = models.LikesCourseComment.objects.all()
    serializer_class = serializers.LikesCourseCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class FAQFrequentlyViewSet(ModelViewSet):
    queryset = models.FAQFrequently.objects.all()
    serializer_class = serializers.FAQFrequentlySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class AskedQuestionViewSet(ModelViewSet):
    queryset = models.AskedQuestion.objects.all()
    serializer_class = serializers.AskedQuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class SeasonViewSet(ModelViewSet):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class MeetingViewSet(ModelViewSet):
    queryset = models.Meeting.objects.all()
    serializer_class = serializers.MeetingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class ExamViewSet(ModelViewSet):
    queryset = models.Exam.objects.all()
    serializer_class = serializers.ExamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class ExamScoreViewSet(ModelViewSet):
    queryset = models.ExamScore.objects.all()
    serializer_class = serializers.ExamScoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class FestivalViewSet(ModelViewSet):
    queryset = models.Festival.objects.all()
    serializer_class = serializers.FestivalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CourseCommentViewSet(ModelViewSet):
    queryset = models.CourseComment.objects.all()
    serializer_class = serializers.CourseCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
