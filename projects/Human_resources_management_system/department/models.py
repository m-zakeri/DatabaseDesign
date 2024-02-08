from django.db import models
from personels.models import Personel


class Department(models.Model):

    director = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=45, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.name}"
    

class Building(models.Model):

    city = models.CharField(max_length=45, null=True, blank=True)
    zone = models.IntegerField(default=0)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "building"
        verbose_name_plural = "buildings"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.city}"
    

class BuildingDepartment(models.Model):

    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="building_department")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="building_department")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "building department"
        verbose_name_plural = "building departments"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"{self.building} - {self.department}"
    