from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'language', views.LanguageViewSet, basename='language')
router.register(r'course-label', views.LabelViewSet, basename='label')
router.register(r'course-category', views.CategoryViewSet, basename='category')
router.register(r'course', views.CourseViewSet, basename='course')
router.register(r'course-description', views.DescriptionViewSet, basename='course_description')
router.register(r'course-like', views.CourseLikeViewSet, basename='course_like')
router.register(r'course-certificate', views.CertificateViewSet, basename='course_certificate')
router.register(r'coupon-code', views.CouponCodeViewSet, basename='coupon_code')

router.register(r'like-course-comment', views.LikesCourseCommentViewSet, basename='like_course_comment')
router.register(r'FAQ-Frequently', views.FAQFrequentlyViewSet, basename='FAQ_Frequently')
router.register(r'Asked-Question', views.AskedQuestionViewSet, basename='Asked_Question')
router.register(r'season', views.SeasonViewSet, basename='season')
router.register(r'meeting', views.MeetingViewSet, basename='meeting')
router.register(r'exam', views.ExamViewSet, basename='exam')
router.register(r'exam-score', views.ExamScoreViewSet, basename='exam_score')
router.register(r'festival', views.FestivalViewSet, basename='festival')
router.register(r'course-comment', views.CourseCommentViewSet, basename='course_comment')

urlpatterns = [
    path('', include(router.urls))
]
