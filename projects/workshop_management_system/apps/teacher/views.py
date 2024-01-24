from django.shortcuts import render
from django.views.generic import ListView
from . import models


class TeacherListView(ListView):
    model = models.Teacher
    queryset = models.Teacher.objects.filter(is_valid=True)
    paginate_by = 1

