from django.db import models
from users.models import User


class Position(models.Model):
    
    name = models.CharField(max_length=45, null=True, blank=True)
    job_title = models.CharField(max_length=45, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "position"
        verbose_name_plural = "positions"

    def __str__(self) -> str:
        return f"{self.name} - {self.job_title}"
    

class Personel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="personels")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, related_name="personels", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "personel"
        verbose_name_plural = "personels"

    def __str__(self) -> str:
        return f"{self.user.username} - personel"


class VacationRequest(models.Model):

    personel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="vacation_requests")
    description = models.TextField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    vacation_start = models.DateTimeField(null=True, blank=True)
    vacation_end = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "vacation request"
        verbose_name_plural = "vacation reqeusts"

    def __str__(self) -> str:
        return f"{self.personel} - vacation_request"


class Payroll(models.Model):

    personel = models.ForeignKey(Personel, on_delete=models.PROTECT, related_name="payrolls")
    salary = models.IntegerField(default=0)
    reward = models.IntegerField(default=0)
    pay_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "payroll"
        verbose_name_plural = "payrolls"

    def __str__(self) -> str:
        return f"{self.personel} - {self.salary}"


class PerformanceReview(models.Model):

    reviewer = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="performance_reviewer")
    personel = models.ForeignKey(Personel, on_delete=models.CASCADE, related_name="reviewed")
    description = models.TextField(null=True, blank=True)
    score = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "performance review"
        verbose_name_plural = "performance reviews"

    def __str__(self) -> str:
        return f"per:{self.personel} - rev:{self.reviewer}"
