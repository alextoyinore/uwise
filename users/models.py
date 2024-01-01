from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, default='', blank=False) 
    country = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.CharField(max_length=6, default='', blank=True)
    photo = models.URLField(default=''),
    current_job_field = models.CharField(max_length=100, default='', blank=True)
    desired_job_field = models.CharField(max_length=100, default='', blank=True)
    current_job = models.CharField(max_length=100, default='', blank=True)
    desired_job = models.CharField(max_length=100, default='', blank=True)
    academic_level = models.ForeignKey('AcademicLevel', on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey('Organization', default=None, null=True, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_facilitator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_subscriber = models.BooleanField(default=False)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
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

# Accessible only to Super Admins
class AcademicLevel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title

class Organization(models.Model):
    fullname = models.CharField(max_length=150, null=False, blank=False)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    organization_name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.URLField(default='')
    region = models.CharField(max_length=100, default='', null=True, blank=True)
    url = models.URLField(null=False, blank=False)
    work_email = models.EmailField(null=False, blank=False)
    type = models.ForeignKey('OrganizationType', on_delete=models.CASCADE, null=False, blank=False)
    size = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name
    
# Accessible only to Super Admins
class OrganizationType(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title
    

class Subscription(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False, default=None)
    date_of_subscription = models.DateField()
    subscription_renewal_date = models.DateField()
    subsciption_type = models.ForeignKey('SubscriptionType', on_delete=models.CASCADE, null=False, blank=False, default=None)

    def __str__(self) -> str:
        return self.user


# Accessible to only Super Admins
class SubscriptionType(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, default='')
    recurrent_type = models.ForeignKey('SubscriptionRecurrentType', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.SlugField(max_length=1000)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

# Accessible to only Super Admins
class SubscriptionRecurrentType(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    time_period = models.BigIntegerField()
    description = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return self.title

