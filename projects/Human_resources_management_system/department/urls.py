from django.urls import path
from .views import DepartmentList, BuildingList, DirectorDepartment


urlpatterns = [
    path("", DepartmentList.as_view(), name="department-list"),
    path("buildings/", BuildingList.as_view(), name="building-list"),
    path("director/<str:director>/", DirectorDepartment.as_view(), name="director-department")
]
