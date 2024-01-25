from django.db import models
from authAPI.models import User, Organization


# Create your models here.
class Field(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Specialization(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    description = models.TextField()
    courses = models.ManyToManyField('Course', related_name='specialization_courses', blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SpecializationCourse(models.Model):
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.specialization.title


class Course(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    facilitators = models.ManyToManyField(User, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, swappable=True, null=True, blank=True)
    level = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CourseLevel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    week = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Reading(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    reading = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, null=True)
    video = models.URLField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.video


class Image(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.URLField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.image


class Audio(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    audio = models.URLField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.audio


class Quiz(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=1000, null=False)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=False, related_name='questions')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=1000, null=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, related_name='answers')
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.answer
