from django.db import models


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', on_delete=models.SET_NULL, null=True, blank=True)
    languages = models.ManyToManyField('Language', on_delete=models.SET_NULL, null=True, blank=True)
    modules = models.ManyToManyField('Module', on_delete=models.SET_NULL, null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
