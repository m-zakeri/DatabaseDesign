import random
import uuid

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import login, authenticate, logout
from . import models


class LoginView(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')

        form = forms.LoginForm()
        return render(request, 'account/sign-in.html', context={'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            next_page = request.GET.get('next')

            user = authenticate(request=request, username=cd['username'], password=cd['password'])
            login(request, user)
            if next_page:
                return redirect(next_page)
            return redirect('/')

        return render(request, 'account/sign-in.html', context={'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')
        form = forms.RegisterForm()
        return render(request, 'account/sign-up.html', context={'form': form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            token = str(uuid.uuid4())
            self.request.session['token'] = token
            randcode = random.randint(10000, 99999)
            subject = 'Register'
            message = f'Hi {cd["username"]}, your verification code for university online is: {randcode}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['email']])

            models.NewUser.objects.create(username=cd['username'], email=cd['email'], password=cd['password'],
                                          confirm_password=cd['confirm_password'], token=token, randcode=randcode)

            return redirect('account_app:verify_email')
        return render(request, 'account/sign-up.html', context={'form': form})


class VerifyEmail(View):
    def get(self, request):
        if not self.request.session.get('token') or self.request.user.is_authenticated:
            return redirect('/')
        form = forms.VerifyEmailForm()
        return render(request, 'account/verify_email.html', context={'form': form})

    def post(self, request):
        form = forms.VerifyEmailForm(request.POST)
        if form.is_valid():
            try:
                token = self.request.session['token']
                new_user = models.NewUser.objects.get(token=token)
                user, is_valid = models.User.objects.get_or_create(username=new_user.username, email=new_user.email)
                user.set_password(new_user.password)
                user.save()
                new_user.delete()
                login(request, user)
                return redirect('/')
            except models.NewUser.DoesNotExist:
                form.add_error('randcode', 'code is wrong.')
                return render(request, 'account/verify_email.html', context={'form': form})

            except:
                return redirect('/')

        return render(request, 'account/verify_email.html', context={'form': form})
