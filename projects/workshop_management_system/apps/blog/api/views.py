from rest_framework.viewsets import ModelViewSet
from apps.blog import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser


class BlogCategoryViewSet(ModelViewSet):
    queryset = models.BlogCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class BlogLabelViewSet(ModelViewSet):
    queryset = models.BlogLabel.objects.all()
    serializer_class = serializers.LabelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class BlogViewSet(ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class DescriptionViewSet(ModelViewSet):
    queryset = models.BlogDescription.objects.all()
    serializer_class = serializers.DescriptionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CommentViewSet(ModelViewSet):
    queryset = models.BlogComment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)


class LikeViewSet(ModelViewSet):
    queryset = models.LikesBlogComment.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
