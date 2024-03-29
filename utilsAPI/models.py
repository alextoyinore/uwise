from django.db import models
from authAPI.models import User, Facilitator
from courseAPI.models import Course, Class


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    description = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

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


class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    organization = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} {self.message}'


class Review(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, swappable=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    facilitator = models.ForeignKey(Facilitator, on_delete=models.SET_NULL, null=True, blank=True)
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.review
    
    class Meta:
        unique_together = ('user', 'course')



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)
    facilitator = models.ForeignKey(Facilitator, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()
    
    class Meta:
        unique_together = ('user', 'course')



class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    the_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.DecimalField(max_digits=2, decimal_places=2, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grade


class Note(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    note = models.TextField()
    the_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.title + " " + self.note


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='message_sender')
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,  related_name='message_receiver')
    message = models.TextField()
    the_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender.get_full_name()} - {self.receiver.get_full_name()} - {self.message}'


class Announcement(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    the_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Only accessible to Super Admins
class MaritalStatus(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)
        verbose_name_plural = 'Marital Statuses'

    def __str__(self):
        return self.title


# Accessible only to Super Admins
class Gender(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, default=None, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False, auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self) -> str:
        return self.course.title
    
    