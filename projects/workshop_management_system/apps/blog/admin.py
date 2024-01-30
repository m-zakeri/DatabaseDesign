from django.contrib import admin
from .models import *


@admin.register(BlogCategory)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_publish', 'show_image')
    search_fields = ('name',)
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('subject', 'caption', 'is_publish', 'show_image')
    search_fields = ('subject', 'caption')
    list_filter = ('is_publish',)
    list_editable = ('is_publish',)
    prepopulated_fields = {'slug': ('subject',)}


@admin.register(BlogDescription)
class DescriptionBlogAdmin(admin.ModelAdmin):
    list_display = ('blog', 'subject', 'content')
    search_fields = ('subject', 'content')


@admin.register(BlogComment)
class CommentBlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'message', 'is_publish')
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)


@admin.register(LikesBlogComment)
class LikeCommentBlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')


admin.site.register(BlogLabel)
