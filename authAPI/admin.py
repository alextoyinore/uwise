from django.contrib import admin

from authAPI.models import *

from authAPI.models import Organization, Referral, Facilitator


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


@admin.register(Organization)
class Organization(admin.ModelAdmin):
    list_display = ('name', 'type', 'website', 'size')
    search_fields = ('name', 'contact_email')


@admin.register(OrganizationType)
class OrganizationType(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('user', 'referrer',)


@admin.register(Facilitator)
class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_facilitator', 'date_upgraded')
    search_fields = ('user',)

