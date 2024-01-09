from django.contrib import admin

from users.models import *

from users.models import Organization


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('last_name', 'email')
    list_filter = ('email', 'first_name')


@admin.register(AcademicLevel)
class AcademicLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)


@admin.register(UserAcademicLevel)
class UserAcademicLevelAdmin(admin.ModelAdmin):
    list_display = ('user', 'academic_level')
    search_fields = ('user',)


@admin.register(Organization)
class Organization(admin.ModelAdmin):
    list_display = ('fullname', 'organization_name', 'type', 'work_email', 'url', 'size')
    search_fields = ('organization_name', 'work_email')


@admin.register(OrganizationType)
class OrganizationType(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)


@admin.register(Gender)
class Gender(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)


@admin.register(UserGender)
class UserGender(admin.ModelAdmin):
    list_display = ('user', 'gender')
    search_fields = ('user',)
