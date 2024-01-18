from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import login, authenticate


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



