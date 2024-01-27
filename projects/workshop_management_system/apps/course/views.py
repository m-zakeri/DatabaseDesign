from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from . import models


class CourseListView(ListView):
    model = models.Course
    queryset = models.Course.objects.filter(is_publish=True).order_by('-created_at')
    paginate_by = 8


class LikeCoureseView(View, LoginRequiredMixin):
    def get(self, request, id):
        try:
            like = models.CourseLikes.objects.get(course_id=id, user_id=self.request.user.id)
            like.delete()
            return JsonResponse({'response': 'dislike'})
        except:
            models.CourseLikes.objects.create(course_id=id, user_id=self.request.user.id)
            return JsonResponse({'response': 'like'})
