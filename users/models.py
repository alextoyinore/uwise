from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager


ACADEMIC_LEVEL = [
        ('degree', 'Degree'),
        ('masters', 'Masters'),
        ('undergraduate', 'Undergraduate'),
        ('doctorate', 'Doctorate'),
        ('highschool', 'High School'),
        ('other', 'Other'),
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
    academic_level = models.CharField(max_length=100, default=None, choices=ACADEMIC_LEVEL)
    is_student = models.BooleanField(default=False)
    is_facilitator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_subscriber = models.BooleanField(default=False)

    
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
    

class Subscriber(models.Model):
    user = models.OneToOneField('User', on_delete=models.DO_NOTHING, null=False, blank=False, default=None)
    date_of_subscription = models.DateField()
    subscription_renewal_date = models.DateField()
    subsciption_type = models.ForeignKey('SubscriptionType', on_delete=models.DO_NOTHING, null=False, blank=False, default=None)

    def __str__(self) -> str:
        return self.user


class SubscriptionType(models.Model):
    SUBSCRIPTION_TYPE = [
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('premium', 'Premium'),
    ]
    name = models.CharField(max_length=100, default=None, choices=SUBSCRIPTION_TYPE)
    RECURRENT_TYPE = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly')
    ]
    recurrent_type = models.CharField(max_length=100, default=None, choices=RECURRENT_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.SlugField(max_length=5000)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
