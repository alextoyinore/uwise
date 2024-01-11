from django.contrib import admin
from .models import *

from courseAPI.models import Course, Module


# Register your models here.
@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'level', 'active', 'field')
    search_fields = ('title', 'level', 'active', 'field')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'week', 'description', 'course')
    search_fields = ('title', 'course')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'module', 'date')
    search_fields = ('title', 'video',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'module', 'date')
    search_fields = ('title', 'image',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question')
    search_fields = ('answer', 'question', 'date',)


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'reading', 'module', 'active')
    search_fields = ('title', 'module', 'active')


@admin.register(Specialization)
class Specialization(admin.ModelAdmin):
    list_display = ('title', 'field')
    search_fields = ('title', 'field')


@admin.register(SpecializationCourse)
class SpecializationCourseAdmin(admin.ModelAdmin):
    list_display = ('course',)
    search_fields = ('course',)
