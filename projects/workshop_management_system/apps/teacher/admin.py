from .models import *

from .filter_admin import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'gender', 'is_valid']
    search_fields = ('user',)
    list_filter = ('is_valid', GenderFilter)
    list_editable = ('is_valid',)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'name', 'work_phone')
    search_fields = ('teacher','name', 'work_phone')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'name', 'description')
    search_fields = ('teacher',)


@admin.register(LevelEducation)
class LevelEducationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'name_university', 'graduation', 'Academic_discipline')
    search_fields = ('teacher',)
