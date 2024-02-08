from django.urls import path
from .views import ResumeList, ResumeDetail


urlpatterns = [
    path("", ResumeList.as_view(), name="resume-list"),
    path("detail/<str:username>/", ResumeDetail.as_view(), name="resume-detail")
]
