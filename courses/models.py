from django.db import models

import users.models
import utils.models


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    tags = models.ManyToManyField(utils.models.Tag, on_delete=models.SET_NULL, null=True, blank=True)
    languages = models.ManyToManyField(utils.models.Language, on_delete=models.SET_NULL, null=True, blank=True)
    modules = models.ManyToManyField('Module', on_delete=models.SET_NULL, null=True, blank=True)
    instructor = models.ForeignKey(users.models.User, on_delete=models.CASCADE, null=False, blank=False)
    organization = models.ForeignKey(users.models.Organization, on_delete=models.CASCADE, null=False, blank=False)
    level = models.ForeignKey(utils.models.CourseLevel, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title


class Module(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
