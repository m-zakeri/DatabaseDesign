from django.urls import path
from .views import (PersonelList, VacationRequestList,
                     PayrollList, PerformanceReviewList, PersonelDetail)


urlpatterns = [
    path("", PersonelList.as_view(), name="personel-list"),
    path("detail/<str:username>/", PersonelDetail.as_view(), name="personel-datail"),
    path("vacation_requests/", VacationRequestList.as_view(), name="vacation-requests"),
    path("payroll/", PayrollList.as_view(), name="payroll"),
    path("performance_review/", PerformanceReviewList.as_view(), name="performance-review")
]
