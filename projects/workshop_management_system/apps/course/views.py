from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse

from . import models, madul
from apps.account.models import User


class CourseListView(ListView):
    model = models.Course
    queryset = models.Course.objects.filter(is_publish=True).order_by('-created_at')
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = models.Language.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return madul.filter_course(self.request, queryset)


class CourseDetailView(DetailView):
    model = models.Course
    queryset = models.Course.objects.filter(is_publish=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = get_object_or_404(models.Course, slug=self.kwargs['slug']).category.all()
        suggested_courses = models.Course.objects.filter(is_publish=True, category__in=categories).distinct().exclude(
            slug=self.kwargs['slug'])
        last_two_courses = models.Course.objects.filter(is_publish=True).order_by('-created_at')[:2]

        context['suggested_courses'] = suggested_courses
        context['last_two_courses'] = last_two_courses
        return context

    def post(self, request, **kwargs):
        message = request.POST.get('message')
        score = request.POST.get('score')
        question = request.POST.get('question')

        try:
            course = models.Course.objects.get(slug=self.kwargs['slug'])
            if message and score:
                models.CourseComment.objects.create(user=self.request.user, score=score, message=message,
                                                    course=course, is_publish=True)
            if question:
                models.AskedQuestion.objects.create(user=request.user, question=question, course=course,
                                                    is_publish=True)

            return redirect(reverse('course_app:course_detail', kwargs={'slug': self.kwargs['slug']}))
        except:
            raise Http404('')


class LikeCourseView(View, LoginRequiredMixin):
    def get(self, request, id):
        try:
            like = models.CourseLikes.objects.get(course_id=id, user_id=self.request.user.id)
            like.delete()
            response = 'dislike'
        except:
            models.CourseLikes.objects.create(course_id=id, user_id=self.request.user.id)
            response = 'like'
        finally:
            return JsonResponse({'response': response})


class LikeCourseCommentView(View, LoginRequiredMixin):
    def get(self, request, id):
        try:
            like = models.LikesCourseComment.objects.get(comment_id=id, user_id=self.request.user.id)
            like.delete()
            response = 'dislike'
        except:
            models.LikesCourseComment.objects.create(comment_id=id, user_id=self.request.user.id)
            response = 'like'

        finally:
            return JsonResponse({'response': response})
