from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from . import madule
from apps.course.models import Course, CourseCategory


class TeacherListView(ListView):
    model = models.Teacher
    queryset = models.Teacher.objects.filter(is_valid=True)
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        return madule.filter_teacher(self.request, queryset)


class TeacherDetailView(DetailView):
    model = models.Teacher
    queryset = models.Teacher.objects.filter(is_valid=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Course.objects.filter(is_publish=True, teacher__id=self.kwargs['pk']).values_list(
            'category').distinct()
        related_teachers = models.Teacher.objects.filter(course__category__in=categories).exclude(
            id=self.kwargs['pk']).distinct()

        context['related_teachers'] = related_teachers
        return context
