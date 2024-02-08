from django.db import models
from personels.models import Personel
from department.models import Building


class Course(models.Model):

    instructor = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="courses")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=45, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self) -> str:
        return f"{self.title}"


class PersonelCourse(models.Model):

    personel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="personel_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="personel_courses")
    score = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "personel course"
        verbose_name_plural = "personel courses"

    def __str__(self) -> str:
        return f"{self.personel} - {self.course}"
    