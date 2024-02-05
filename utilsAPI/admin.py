from django.contrib import admin

from utilsAPI.models import *

from utilsAPI.models import Review, Rating, Grade, Note, Message, Testimonial, Announcement


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'title', 'review')
    search_fields = ('user', 'course',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'date')
    search_fields = ('user', 'course', 'rating',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'grade', 'date',)
    search_fields = ('user', 'course', 'grade',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'title', 'note',)
    search_fields = ('user', 'course',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'message', 'date',)
    search_fields = ('user', 'course', 'date',)


@admin.register(Gender)
class Gender(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'date')
    search_fields = ('title', 'user',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'date', 'course', 'user')
    search_fields = ('title', 'user', 'course', 'message', 'date')
