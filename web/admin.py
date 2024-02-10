from django.contrib import admin

from web.models import CourseCarousel, StaticPage, FooterNav, FooterLink


# Register your models here.
@admin.register(CourseCarousel)
class CourseCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'content')
    search_fields = ('title',)


@admin.register(FooterNav)
class FooterNavAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'url')
    search_fields = ('title',)

