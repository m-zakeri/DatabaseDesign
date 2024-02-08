from django.db import models
from users.models import User


class Resume(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "resume"
        verbose_name_plural = "resumes"
    
    def __str__(self) -> str:
        return f"{self.user} - resume"


class Degree(models.Model):

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="degrees")
    degree = models.CharField(max_length=45, null=True, blank=True)
    institute = models.CharField(max_length=45, null=True, blank=True)
    field = models.CharField(max_length=45, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "degree"
        verbose_name_plural = "degrees"

    def __str__(self) -> str:
        return f"{self.resume} - {self.degree}"
    

class Skill(models.Model):

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=45, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"

    def __str__(self) -> str:
        return f"{self.resume} - {self.title}"
    

class Experinece(models.Model):

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="experiences")
    position = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=45, null=True, blank=True)
    years_of_experience = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "experience"
        verbose_name_plural = "experiences"

    def __str__(self) -> str:
        return f"{self.resume} - {self.position}"
