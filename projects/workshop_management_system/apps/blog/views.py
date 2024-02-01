from django.shortcuts import render
from django.views.generic import ListView
from . import models


class BlogListView(ListView):
    model = models.Blog
    queryset = models.Blog.objects.filter(is_publish=True)
    paginate_by = 1
