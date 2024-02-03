from django.shortcuts import render, redirect
from admin_volt.forms import (
    RegistrationForm,
    LoginForm,
    UserPasswordResetForm,
    UserPasswordChangeForm,
    UserSetPasswordForm,
)
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordChangeView,
    PasswordResetConfirmView,
)
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


# Create your views here.
#
#
def dashboard(request):
    context = {"segment": "dashboard"}
    return render(request, "pages/dashboard/dashboard.html", context)
