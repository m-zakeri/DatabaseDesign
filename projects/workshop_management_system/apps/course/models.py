from django.db import models
from django.utils.html import format_html

from apps.account.models import User, Card
from apps.teacher.models import Teacher
from apps.customer.models import Customer
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


class CourseLabel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')


class CourseCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    image = models.ImageField(upload_to='image/category/course', verbose_name=_('Image'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subs',
                               verbose_name=_('Parent'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def show_image(self):
        return format_html(f"<img src={self.image.url} width='50px' height='50px' >")

    show_image.short_description = _('image')


class Course(models.Model):
    type_course = (
        ('Face to face class', _('IN PERSON')),
        ('Online class', _('ONLINE')),
        ('Online and Face-to-face classes', _('IN PERSON AND ONLINE'))
    )
    levels = (
        ('All levels', _('All levels')),
        ('Beginner', _('Beginner')),
        ('Preliminary', _('Preliminary')),
        ('Advanced', _('Advanced')),

    )
    states = (
        ('The course has not started', _('The course has not started')),
        ('Uploading', _('Uploading')),
        ('Completion of the course', _('Completion of the course'))

    )

    name = models.CharField(max_length=50, verbose_name=_('Name'))
    caption = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('Caption'))
    image = models.ImageField(upload_to='image/course', verbose_name=_('Image'))
    introduction_video = models.FileField(upload_to='video/course', null=True, blank=True,
                                          verbose_name=_('Introduction video'))
    level = models.CharField(max_length=50, choices=levels, default='All levels', verbose_name=_('Level'))
    state = models.CharField(max_length=50, choices=states, default='Start of the course', verbose_name=_('State'))
    slug = models.SlugField(verbose_name=_('Slug'))

    language = models.ManyToManyField(Language, related_name='course', verbose_name=_('Language'))
    label = models.ManyToManyField(CourseLabel, related_name='course', verbose_name=_('Label'))
    category = models.ManyToManyField(CourseCategory, related_name='course', verbose_name=_('Category'))
    teacher = models.ManyToManyField(Teacher, related_name='course', verbose_name=_('Teacher'))
    customer = models.ManyToManyField(Customer, blank=True, related_name='course', verbose_name=_('Costumer'))

    number_customer = models.PositiveIntegerField(default=0, verbose_name=_('Costumer Number'))
    number_video = models.PositiveIntegerField(default=0, verbose_name=_('Number Of Video'))
    video_time = models.DurationField(default=0, verbose_name=_('Video Time'))
    course_start_date = models.DateField(verbose_name=_('Course Start Date'))

    is_exam = models.BooleanField(default=False, verbose_name=_('Is exam'))
    is_graduation = models.BooleanField(default=False, verbose_name=_('Is Graduation'))
    registering_open = models.BooleanField(default=True, verbose_name=_('Registering Open'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))

    price = models.FloatField(default=0, verbose_name=_('Price'))
    discount = models.FloatField(default=0, verbose_name=_('Discount'))
    start_discount = models.DateTimeField(null=True, blank=True, verbose_name=_('Start Discount'))
    end_discount = models.DateTimeField(null=True, blank=True, verbose_name=_('End Discount'))
    total_points = models.FloatField(default=0, verbose_name=_('Total Points'))
    type = models.CharField(max_length=50, choices=type_course, default='Online class', verbose_name=_('Type'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    def show_image(self):
        return format_html(f"<img src={self.image.url} width='50px' height='50px' >")

    show_image.short_description = _('image')

    def apply_discount(self):
        return self.price - ((self.price * self.discount) / 100)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class CourseDescription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='descriptions', verbose_name=_('Course'))
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


class CourseDescriptionItem(models.Model):
    course_description = models.ForeignKey(CourseDescription, on_delete=models.CASCADE, related_name='item',
                                           verbose_name='Course Description')
    text = models.TextField(verbose_name=_('Text'))
    is_label = models.BooleanField(default=False, verbose_name=_('Is Label'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Description Item')
        verbose_name_plural = _('Description Items')


class CourseLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_course', verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='like', verbose_name=_('Course'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('Likes')


class CourseCertificate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificate', verbose_name=_('Course'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    certificate_image = models.FileField(upload_to='document/certificate/course', verbose_name=_('Certificate Image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')


class CouponCode(models.Model):
    user_costumer = models.ManyToManyField(Customer, related_name='coupon_code', verbose_name=_('User Costumer'))
    course = models.ManyToManyField(Course, related_name='coupon_code', verbose_name=_('Course'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    discount = models.FloatField(verbose_name=_('Discount'))
    number_discount = models.PositiveIntegerField(verbose_name=_('Number Of Discount'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    valid_from = models.DateTimeField(verbose_name=_('Valid Form'))
    valid_to = models.DateTimeField(verbose_name=_('Valid To'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Coupon Code')
        verbose_name_plural = _('Coupon Codes')


class CourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_comment', verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comment', verbose_name=_('Course'))
    message = models.CharField(max_length=300, verbose_name=_('Message'))
    score = models.FloatField(default=0, verbose_name='Score')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subs',
                               verbose_name=_('Parent'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.user}-> {self.message[:30]} '

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class LikesCourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_course_comment', verbose_name=_('User'))
    comment = models.ForeignKey(CourseComment, on_delete=models.CASCADE, related_name='like', verbose_name=_('Comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('The Like Of The Course Comment')
        verbose_name_plural = _('The Like Of The Course Comments')


class FAQFrequently(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='fa_frequently', verbose_name=_('Course'))
    question = models.CharField(max_length=100, verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('Frequently Asked Question')
        verbose_name_plural = _('Frequently Asked Questions')


class AskedQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ask_question', verbose_name=_('Course'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ask_question_course', verbose_name=_('User'))
    question = models.CharField(max_length=300, verbose_name=_('Question'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subs',
                               verbose_name=_('Parent'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('Frequently Asked Question')
        verbose_name_plural = _('Frequently Asked Questions')


class Season(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='season', verbose_name=_('Course'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')


class Meeting(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='meeting', verbose_name=_('Season'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    location_and_time = models.TextField(verbose_name=_('Location And Time'))
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('Link'))
    video = models.FileField(upload_to='video/meeting', verbose_name=_('Video'))
    video_time = models.DurationField(verbose_name=_('Video Time'))

    file = models.FileField(upload_to='file/document', verbose_name=_('File'))
    free = models.BooleanField(default=False, verbose_name=_('Is Free'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Meeting')
        verbose_name_plural = _('Meetings')


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exam', verbose_name=_('Course'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    start_exam = models.DateTimeField(verbose_name=_('Exam Start Date And Time'))
    link = models.URLField(null=True, blank=True, verbose_name=_('Link'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')


class ExamScore(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='Score', verbose_name=_('Exam'))
    costumer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='exam', verbose_name=_('Costumer'))
    score = models.FloatField(verbose_name=_('Score'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Exam Score')
        verbose_name_plural = _('Exam Scores')


class Festival(models.Model):
    course = models.ManyToManyField(Course, related_name='festival', verbose_name=_('Course'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    image = models.ImageField(upload_to='image/festival', verbose_name=_('Image'))
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(verbose_name=_('End Time'))
    is_publish = models.BooleanField(default=False, verbose_name=_('Is Publish'))
    registering_open = models.BooleanField(default=True, verbose_name=_('Registering Open'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    def show_image(self):
        return format_html(f"<img src={self.image.url} width='50px' height='50px'>")

    show_image.short_description = _('image')

    class Meta:
        verbose_name = _('Festival')
        verbose_name_plural = _('Festivals')
