from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("users/", include("users.urls")),
    path("personels/", include("personels.urls")),
    path("course/", include("course.urls")),
    path("department/", include("department.urls")),
    path("resume/", include("resume.urls")),
    path("meeting/", include("interview_meeting.urls")),
    path("interview/", include("interview_meeting.urls"))
]
