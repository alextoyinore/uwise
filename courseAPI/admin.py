from django.contrib import admin
from .models import *

from courseAPI.models import Course, Lesson, Field, UserCourse, CourseFacilitator


# Register your models here.
@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'level', 'is_active', 'field')
    search_fields = ('title', 'level', 'active', 'field')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'week', 'description', 'price', 'course')
    search_fields = ('title', 'course')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'lesson', 'date')
    search_fields = ('title', 'video',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'lesson', 'date')
    search_fields = ('title', 'image',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson')
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
    list_display = ('title', 'reading', 'lesson', 'is_active')
    search_fields = ('title', 'lesson', 'active')


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('title', 'field')
    search_fields = ('title', 'field')


@admin.register(SpecializationCourse)
class SpecializationCourseAdmin(admin.ModelAdmin):
    list_display = ('course',)
    search_fields = ('course',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title', 'is_active')


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date')
    search_fields = ('date', 'user', 'course')


@admin.register(CourseFacilitator)
class CourseFacilitatorAdmin(admin.ModelAdmin):
    list_display = ('facilitator', 'course', 'date')
    search_fields = ('facilitator', 'course', 'date')
