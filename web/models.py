from django.db import models

from courseAPI.models import Course


# Create your models here.

class CourseCarousel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Carousel Title', null=False, blank=False)
    courses = models.ManyToManyField(Course)
    date = models.DateField(auto_now=True, verbose_name='Date', null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name='active', null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class StaticPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    url_name = models.CharField(max_length=200, verbose_name='url_name', null=False, blank=False)
    content = models.TextField(verbose_name='description', null=False, blank=False)
    date = models.DateField(auto_now=True, verbose_name='date')
    is_active = models.BooleanField(default=True, verbose_name='active', null=False)
    slug = models.SlugField(null=True, blank=True)
    is_model_page = models.BooleanField(default=False)

    def __str__(self):
        return self.url_name


class FooterNav(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    is_active = models.BooleanField(default=True, verbose_name='active', null=False)
    footer_links = models.ManyToManyField('StaticPage', verbose_name='static_pages', related_name='static_pages')

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    url_name = models.CharField(max_length=200, verbose_name='url_name', null=False)
    url = models.URLField(default='', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='active', null=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

