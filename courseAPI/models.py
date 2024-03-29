from django.db import models
from rest_framework.exceptions import ValidationError

from authAPI.models import User, Organization, Facilitator


# Create your models here.
class Field(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title    


class SpecializationCourse(models.Model):
    specialization = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='specialization')
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, related_name='specialization_course')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.specialization.title


class Course(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    excerpt = models.TextField(null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    welcome_note = models.TextField(blank=True, null=True)
    intro_video = models.URLField(blank=True, null=True)
    community_link1 = models.URLField(blank=True, null=True)
    community_link2 = models.URLField(blank=True, null=True)
    duration = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='courses', null=False, blank=False)
    image_link = models.URLField(null=True, blank=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    class_interval = models.IntegerField(blank=False, null=False)
    language = models.CharField(max_length=200, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, swappable=True, null=True, blank=True)
    level = models.ForeignKey('CourseLevel', 
                              on_delete=models.SET_NULL, 
                              null=True, blank=True,
                              related_name='course_level')
    course_type = models.ForeignKey('CourseType', 
                              on_delete=models.DO_NOTHING, 
                              related_name='course_type')
    skills = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    objectives = models.TextField(blank=True, null=True)
    next_start_date = models.DateTimeField(null=True, blank=True)
    is_specialization = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_created', 'is_active', 'next_start_date')


class CourseType(models.Model):
    type = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_owner', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user.get_full_name()} {self.course.title}'



class CourseFacilitator(models.Model):
    facilitators = models.ManyToManyField(Facilitator, related_name='facilitators')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='course_facilitated', null=False,
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


class Class(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class_link1 = models.URLField(null=False, blank=False)
    class_link2 = models.URLField(null=True, blank=True)
    resources = models.ForeignKey('Resource', models.CASCADE, related_name='resource_for_class', null=True, blank=True)
    class_number = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False, default='')
    objectives = models.TextField(blank=False, null=False, default='')
    date_created = models.DateField(auto_now=True)
    time_duration = models.IntegerField()
    expiration_date = models.DateField(null=True, blank=True)
    class_did_hold = models.BooleanField()
    facilitator = models.ForeignKey(Facilitator, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    link = models.URLField(max_length=5000, null=False, blank=False)
    images = models.ManyToManyField('Image', related_name='images_for_class')
    videos = models.ManyToManyField('Video', related_name='videos_for_class')
    audios = models.ManyToManyField('Audio', related_name='audios_for_class')
    readings = models.ManyToManyField('Reading', related_name='readings_for_class')
    assessments = models.ManyToManyField('Assessment', related_name='assignments_for_class')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Assessment(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=False, null=False, default='')
    link = models.URLField(max_length=5000, null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    time_duration = models.IntegerField()
    date_due = models.DateTimeField()
    the_class = models.ForeignKey('Class', models.CASCADE, related_name='class_assessment', null=True, blank=True)

    def __str__(self):
        return self.title


class UserClass(models.Model):
    the_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='user_class')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_owner')
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'User Classes'
        unique_together = ('the_class', 'user')

    def __str__(self):
        return f'{self.user.get_full_name()} {self.the_class.title}'


class StudentAttendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    the_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='the_class_student_attended')
    did_attend_class = models.BooleanField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.the_class.title


class FacilitatorAttendance(models.Model):
    facilitator = models.ForeignKey(Facilitator, on_delete=models.CASCADE, related_name='facilitator')
    the_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='the_class_facilitated')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('facilitator', 'the_class')

    def __str__(self):
        return f'{self.the_class.title}'


class Reading(models.Model):
    the_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    link = models.URLField(max_length=5000, null=True, blank=True)
    reading = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    the_class = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    video = models.URLField(max_length=200, null=False, blank=False)
    link = models.URLField(max_length=5000, null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.URLField(max_length=200, null=False, blank=False)
    description = models.TextField()
    link = models.URLField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    the_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Audio(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    audio = models.URLField(max_length=200, null=False, blank=False)
    link = models.URLField(max_length=5000, null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    the_class = models.ForeignKey('Class', on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    link = models.URLField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    the_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=1000, null=False)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=False, related_name='questions')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    link = models.URLField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=1000, null=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, related_name='answer_question')
    link = models.URLField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.answer
