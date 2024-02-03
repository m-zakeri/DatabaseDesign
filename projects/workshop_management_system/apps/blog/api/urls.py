from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'blog-category', views.BlogCategoryViewSet, basename='blog-category'),
router.register(r'blog-label', views.BlogLabelViewSet, basename='blog-label'),
router.register(r'blog', views.BlogViewSet, basename='blog'),
router.register(r'blog-description', views.DescriptionViewSet, basename='blog_description'),
router.register(r'blog-comment', views.CommentViewSet, basename='blog_comment'),
router.register(r'like-blog-comment', views.LikeViewSet, basename='blog_comment_like'),

urlpatterns = [
    path('', include(router.urls))
]
