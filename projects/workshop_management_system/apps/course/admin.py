
from .models import *
from .filter_admin import *

admin.site.register(Language)
admin.site.register(CourseLabel)


@admin.register(CourseCategory)
class CategoryCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_publish', 'show_image')
    search_fields = ('name',)
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'state', 'price', 'show_image')
    search_fields = ('name', LevelFilter, StateFilter)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CourseDescription)
class DescriptionCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject', 'content')
    search_fields = ('subject', 'content')


@admin.register(CourseDescriptionItem)
class DescriptionCourseItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_label')
    list_editable = ('is_label',)
    list_filter = ('is_label',)


@admin.register(CourseLikes)
class LikeCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')


@admin.register(FAQFrequently)
class FAQFrequentlyAdmin(admin.ModelAdmin):
    list_display = ('course', 'question', 'answer')


@admin.register(AskedQuestion)
class AskedQuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'question', 'is_publish')
    search_fields = ('user', 'course')
    list_filter = ('is_publish',)
    list_editable = ('is_publish',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'is_publish')
    search_fields = ('course', 'name')
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('season', 'name', 'location_and_time', 'free', 'is_publish')
    search_fields = ('season', 'name')
    list_editable = ('free', 'is_publish')
    list_filter = ('free', 'is_publish')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'start_exam', 'is_publish')
    search_fields = ('course', 'name')
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)


@admin.register(ExamScore)
class ScoreExamAdmin(admin.ModelAdmin):
    list_display = ('exam', 'costumer', 'score')
    search_fields = ('exam', 'costumer')
    list_editable = ('score',)


@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_publish', 'show_image')
    search_fields = ('name',)
    list_filter = ('is_publish',)
    list_editable = ('is_publish',)


@admin.register(CourseCertificate)
class CertificateCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'name')


@admin.register(CouponCode)
class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'is_active')
    search_fields = ('name',)
    list_editable = ('discount', 'is_active')
    list_filter = ('is_active',)


@admin.register(CourseComment)
class CommentCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'message', 'is_publish')
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)


@admin.register(LikesCourseComment)
class LikeCommentCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')
