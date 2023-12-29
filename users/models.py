from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager


ACADEMIC_LEVEL = [
        ('D', 'Degree'),
        ('M', 'Masters'),
        ('U', 'Undergraduate'),
        ('D', 'Doctorate'),
        ('H', 'High School'),
        ('O', 'Other'),
    ]

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, default='', blank=False) 
    country = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.CharField(max_length=6, default='', blank=True)
    current_job_field = models.CharField(max_length=100, default='', blank=True)
    desired_job_field = models.CharField(max_length=100, default='', blank=True)
    current_job = models.CharField(max_length=100, default='', blank=True)
    desired_job = models.CharField(max_length=100, default='', blank=True)
    is_student = models.BooleanField(default=False)
    is_facilitator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    academic_level = models.CharField(max_length=1, default='D', choices=ACADEMIC_LEVEL)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'is_student',
        'is_facilitator',
        'is_admin',
    ]

    objects = CustomUserManager()

    '''
    Generate username from user provided email
    '''
    def save(self, *args, **kwargs):
        email_username = self.email.split('@')[0]
        email_domain = self.email.split('@')[1].split('.')[0]
        self.username = email_username + email_domain
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()

