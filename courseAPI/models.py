from django.db import models
from rest_framework.exceptions import ValidationError

import authAPI
from authAPI.models import User, Organization


# Create your models here.
class Field(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    link = models.URLField(auto_created=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Specialization(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    link = models.URLField(auto_created=True)
    description = models.TextField()
    objectives = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField('Course', related_name='programme_courses', blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SpecializationCourse(models.Model):
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    link = models.URLField(auto_created=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.specialization.title


class Course(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    excerpt = models.TextField(null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    image = models.URLField(null=True, blank=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    facilitators = models.ManyToManyField(User, blank=False)
    courses = models.ManyToManyField('Course', blank=True, related_name='specialization_courses')
    lessons = models.ManyToManyField('Lesson', blank=True, related_name='course_lessons')
    language = models.CharField(max_length=200, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, swappable=True, null=True, blank=True)
    level = models.CharField(max_length=200, null=False, blank=False)
    skills = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    objectives = models.TextField(blank=True, null=True)
    next_start_date = models.DateTimeField(null=True, blank=True)
    is_specialization = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)
    link = models.URLField(auto_created=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_created', 'is_active', 'next_start_date', 'is_specialization')

    def save(self, *args, **kwargs):
        if not self.is_specialization and self.courses is not None:
            raise ValidationError('This course is not a specialization')
        else:
            super(Course, self).save(*args, **kwargs)


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_owner', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    link = models.URLField(auto_created=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.title


class CourseFacilitator(models.Model):
    facilitator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_facilitator', null=False,
                                    blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_facilitated', null=False,
                               blank=False)
    link = models.URLField(auto_created=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facilitator.get_full_name()

    def save(self, *args, **kwargs):
        if not self.facilitator.is_facilitator:
            raise ValidationError('This user is not a facilitator')
        else:
            super(CourseFacilitator, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date',)


class CourseLevel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    week = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    link = models.URLField(auto_created=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Reading(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    reading = models.TextField(blank=False, null=False)
    link = models.URLField(auto_created=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True)
    video = models.URLField()
    link = models.URLField(auto_created=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.video


class Image(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.URLField()
    link = models.URLField(auto_created=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.image


class Audio(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    audio = models.URLField()
    link = models.URLField(auto_created=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.audio


class Quiz(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    link = models.URLField(auto_created=True)
    date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=1000, null=False)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=False, related_name='questions')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    link = models.URLField(auto_created=True)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=1000, null=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, related_name='answer_question')
    link = models.URLField(auto_created=True)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.answer
