from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from apps.teacher.models import Teacher
from django.conf import settings
from . import forms


class ContactUsView(FormView):
    template_name = 'contact/contact-us.html'
    form_class = forms.CuntactUsForm
    success_url = '/'

    def form_valid(self, form):
        cd = form.cleaned_data
        subject = 'contact us'
        message = f'{cd["message"]}\n name: {cd["name"]} \n email: {cd["email"]}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class AboutUsView(TemplateView):
    template_name = 'contact/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.filter(is_valid=True)
        return context
