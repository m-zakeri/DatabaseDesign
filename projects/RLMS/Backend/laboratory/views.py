from django.shortcuts import render
from .models import *

# Create your views here.


def dashboard(request):
    context = {"segment": "dashboard"}
    return render(request, "pages/dashboard/dashboard.html", context)
