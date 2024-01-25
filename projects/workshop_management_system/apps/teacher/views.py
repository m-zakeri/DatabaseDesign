from django.shortcuts import render
from django.views.generic import ListView
from . import models
from . import filter_teacher


class TeacherListView(ListView):
    model = models.Teacher
    queryset = models.Teacher.objects.filter(is_valid=True)
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        return filter_teacher.filter(self.request, queryset)
