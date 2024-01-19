from django.shortcuts import render
from django.views.generic import TemplateView
from apps.course.models import Course, Festival, CourseCertificate
from apps.customer.models import Customer
from apps.teacher.models import Teacher


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(is_publish=True).order_by('-number_customer')[:8]
        context['festival'] = Festival.objects.filter(is_publish=True).order_by('-created_at').first()
        context['number_customer'] = Customer.objects.filter(is_valid=True).count()
        context['number_course'] = Course.objects.filter(is_publish=True).count()
        context['number_teacher'] = Teacher.objects.filter(is_valid=True).count()
        context['number_certificate'] = CourseCertificate.objects.all().count()

        return context
