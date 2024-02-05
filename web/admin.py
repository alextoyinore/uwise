from django.contrib import admin

from web.models import CourseCarousel, BusinessModel, FooterTitle, FooterLink


# Register your models here.
@admin.register(CourseCarousel)
class CourseCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@admin.register(BusinessModel)
class BusinessModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'description')
    search_fields = ('title',)


@admin.register(FooterTitle)
class FooterTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'url')
    search_fields = ('title',)

