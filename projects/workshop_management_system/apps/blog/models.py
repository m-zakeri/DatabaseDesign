from django.db import models
from django.utils.html import format_html

from apps.account.models import User
from django.utils.translation import gettext_lazy as _


class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField()
    description = models.TextField(null=True,blank=True,verbose_name=_('Description'))
    image = models.ImageField(upload_to='img/category/blog', verbose_name=_('Image'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subs',
                               verbose_name=_('Parent'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    def show_image(self):
        return format_html(f"<img src={self.image.url} width='50px' height='50px'>")

    show_image.short_description = _('image')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class BlogLabel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')


class Blog(models.Model):
    author = models.ManyToManyField(User, related_name='blog', verbose_name=_('Author'))
    subject = models.CharField(max_length=100, verbose_name=_('Subject'))
    caption = models.TextField(null=True, blank=True, verbose_name=_('Caption'))
    slug = models.SlugField()
    image = models.ImageField(upload_to='image/blog', verbose_name=_('Image'))
    category = models.ManyToManyField(BlogCategory, related_name='blog', verbose_name=_('Category'))
    label = models.ManyToManyField(BlogLabel, related_name='blog', verbose_name=_('Label'))

    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.subject}:{self.caption}'

    def show_image(self):
        return format_html(f"<img src={self.image.url} width='50px' height='50px'>")

    show_image.short_description = _('image')

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class BlogDescription(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='description', verbose_name=_('Blog'))
    subject = models.CharField(max_length=100, verbose_name=_('Subject'))
    content = models.TextField(verbose_name=_('Content'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subs',
                               verbose_name=_('Parent'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.subject} -> {self.content[:50]}'

    class Meta:
        verbose_name = _('Description')
        verbose_name_plural = _('Descriptions')


class BlogDescriptionItem(models.Model):
    blog_description = models.ForeignKey(BlogDescription, on_delete=models.CASCADE, related_name='item',
                                         verbose_name=_('Blog Description'))
    text = models.TextField(verbose_name=_('Text'))
    is_label = models.BooleanField(default=False, verbose_name=_('Is Lable'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Description Item')
        verbose_name_plural = _('Description Items')


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment', verbose_name=_('Blog'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment', verbose_name=_('User'))
    message = models.CharField(max_length=300, verbose_name=_('Message'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True, related_name='subs', verbose_name=_('Parent'))

    def __str__(self):
        return f'{self.user} -> {self.message[:30]}'

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class LikesBlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_blog_comment', verbose_name=_('User'))
    comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE, related_name='like', verbose_name=_('Comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('Comment Like')
        verbose_name_plural = _('Comment Likes')

