from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class BlogListView(ListView):
    model = models.Blog
    queryset = models.Blog.objects.filter(is_publish=True)
    paginate_by = 8


class BlogDetailView(DetailView):
    model = models.Blog
    queryset = models.Blog.objects.filter(is_publish=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = models.Blog.objects.get(slug=self.kwargs['slug']).category.all()
        related_blogs = models.Blog.objects.filter(category__in=categories).distinct().exclude(slug=self.kwargs['slug'])
        context['related_blogs'] = related_blogs
        return context
