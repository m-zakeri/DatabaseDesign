from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class LikeCoureseView(View, LoginRequiredMixin):
    def get(self, request, id):
        try:
            like = models.CourseLikes.objects.get(course_id=id, user_id=self.request.user.id)
            like.delete()
            return JsonResponse({'response': 'dislike'})
        except:
            models.CourseLikes.objects.create(course_id=id, user_id=self.request.user.id)
            return JsonResponse({'response': 'like'})
