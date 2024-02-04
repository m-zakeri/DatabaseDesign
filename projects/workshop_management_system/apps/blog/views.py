from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from . import models
from ..account.models import User
from apps.course.templatetags.course_tags import convert_to_shamsi


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

    def post(self, request, **kwargs):
        message = request.POST.get('message')
        parent_id = request.POST.get('parent_id')

        try:
            user = User.objects.get(id=self.request.user.id)

            blog = models.Blog.objects.get(slug=kwargs['slug'])

            comment = models.BlogComment.objects.create(blog=blog, user=self.request.user, message=message,

                                                        parent_id=parent_id, is_publish=True)
            is_parent = False
            if comment.parent_id:
                is_parent = True

            created_at = convert_to_shamsi(comment.created_at)

            return JsonResponse(
                {'IsParent': is_parent, 'ImageUrl': user.image.url, 'id': comment.id, 'FullName': user.full_name(),
                 'message': message, 'ParentId': parent_id, 'createdAt': created_at})
        except:

            return JsonResponse({'response': 'page not found .'})
