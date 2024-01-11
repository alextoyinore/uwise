from django.db import models
import authAPI.models
import courseAPI.models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    description = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField()
    description = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    region = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(authAPI.models.User, on_delete=models.CASCADE)
    course = models.ForeignKey(courseAPI.models.Course, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(authAPI.models.User, on_delete=models.CASCADE)
    course = models.ForeignKey(courseAPI.models.Course, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating


class Grade(models.Model):
    user = models.ForeignKey(authAPI.models.User, on_delete=models.CASCADE)
    course = models.ForeignKey(courseAPI.models.Course, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=2, decimal_places=2, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grade


class Note(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(authAPI.models.User, on_delete=models.CASCADE)
    course = models.ForeignKey(courseAPI.models.Course, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(auto_now=True)
    video_time = models.TimeField()

    def __str__(self):
        return self.note


class Message(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(authAPI.models.User, on_delete=models.CASCADE)
    course = models.ForeignKey(courseAPI.models.Course, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

# Only accessible to Super Admins
class MaritalStatus(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# Accessible only to Super Admins
class Gender(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, default=None, blank=False)

    def __str__(self) -> str:
        return self.title