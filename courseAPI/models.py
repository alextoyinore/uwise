from django.db import models
from rest_framework.exceptions import ValidationError

import authAPI
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
    objectives = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
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
    excerpt = models.TextField(null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    image = models.URLField(null=False, blank=False)
    # image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    language = models.CharField(max_length=200, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, swappable=True, null=True, blank=True)
    level = models.ForeignKey('CourseLevel', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='course_level')
    skills = models.CharField(max_length=200, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    objectives = models.TextField(blank=True, null=True)
    next_start_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_created', 'is_active', 'next_start_date')


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_owner', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.get_full_name()} {self.course.title}'


class CourseFacilitator(models.Model):
    facilitator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_facilitator', null=False,
                                    blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_facilitated', null=False,
                               blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facilitator.get_full_name()

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
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class UserLesson(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='user_lesson')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_owner')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.get_full_name()} {self.lesson.title}'


class Reading(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    reading = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True)
    video = models.URLField(max_length=200, null=False, blank=False)
    # video = models.FileField(upload_to='course/files/lesson/videos/', null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.video


class Image(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.URLField(max_length=200, null=False, blank=False)
    # image = models.FileField(upload_to='course/files/lesson/images/', null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.image


class Audio(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    audio = models.URLField(max_length=200, null=False, blank=False)
    # audio = models.FileField(upload_to='course/files/lesson/audio/', null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.audio


class Quiz(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
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
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, related_name='answer_question')
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.answer
