from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from . import models, madul


class CourseListView(ListView):
    model = models.Course
    queryset = models.Course.objects.filter(is_publish=True).order_by('-created_at')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = models.Language.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return madul.filter_course(self.request, queryset)


class LikeCoureseView(View, LoginRequiredMixin):
    def get(self, request, id):
        try:
            like = models.CourseLikes.objects.get(course_id=id, user_id=self.request.user.id)
            like.delete()
            return JsonResponse({'response': 'dislike'})
        except:
            models.CourseLikes.objects.create(course_id=id, user_id=self.request.user.id)
            return JsonResponse({'response': 'like'})
