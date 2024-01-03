from django.contrib import admin

from utils.models import *


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


@admin.register(CourseLevel)
class CourseLevel(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
