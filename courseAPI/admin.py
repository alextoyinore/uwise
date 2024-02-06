from django.contrib import admin
from .models import *

from courseAPI.models import Course, Class, Field, UserCourse, CourseFacilitator, UserClass


# Register your models here.
@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'level', 'price', 'is_active', 'field')
    search_fields = ('title', 'level', 'active', 'field')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'class_number', 'description', 'price', )
    search_fields = ('title', 'course')


@admin.register(Resource)
class Resource(admin.ModelAdmin):
    list_display = ('title','link', 'the_class')
    search_fields = ('title', 'the_class')


@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('the_class', 'student', 'date')
    search_fields = ('the_class', 'student', 'date')


@admin.register(FacilitatorAttendance)
class FacilitatorAttendanceAdmin(admin.ModelAdmin):
    list_display = ('the_class', 'facilitator', 'date')
    search_fields = ('the_class', 'facilitator', 'date')


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'date_created', 'date_due')
    search_fields = ('title', 'date_created', 'date_due')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'the_class', 'date')
    search_fields = ('title', 'video',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'the_class', 'date')
    search_fields = ('title', 'image',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'the_class')
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
    list_display = ('title', 'reading', 'the_class', 'is_active')
    search_fields = ('title', 'the_class', 'active')


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
    list_display = ('course', 'date')
    search_fields = ('course', 'date')


@admin.register(UserClass)
class Userthe_classAdmin(admin.ModelAdmin):
    list_display = ('the_class', 'user',)
    search_fields = ('the_class', 'user')
