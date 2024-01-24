from django.db import models
from django.contrib.auth.models import AbstractUser

# from utilsAPI.models import Gender, MaritalStatus
from authAPI.manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=20, default='', null=True, blank=True)
    phone = models.CharField(max_length=15, default='', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=100, default='', null=True, blank=True)
    marital_status = models.CharField(max_length=20, default='', null=True, blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.CharField(max_length=10, default='', blank=True)
    image = models.ImageField(upload_to='uploads/users/', default='', null=True, blank=True)
    current_work_field = models.CharField(max_length=100, default='', blank=True)
    desired_work_field = models.CharField(max_length=100, default='', blank=True)
    current_job_title = models.CharField(max_length=100, default='', blank=True)
    desired_job_title = models.CharField(max_length=100, default='', blank=True)
    academic_level = models.CharField(max_length=100, default='', blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=2000, default='', null=True, blank=True)
    organization = models.CharField(max_length=100, default='', null=True, blank=True)
    is_facilitator = models.BooleanField(default=False)

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

    def __str__(self) -> str:
        return self.get_full_name()


# Accessible only to Super Admins
class AcademicLevel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title


class Organization(models.Model):
    # REGISTERER DATA
    contact_name = models.CharField(max_length=150, null=False, blank=False)
    contact_job_title = models.CharField(max_length=100, null=False, blank=False)
    contact_email = models.EmailField(null=False, blank=False)
    contact_phone = models.CharField(max_length=15, null=False, blank=False)
    contact_image = models.ImageField(default='', null=True, blank=True)

    # ORGANIZATION DATA
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(default='', upload_to='')
    address = models.CharField(max_length=500, default='', null=True, blank=True)
    website = models.URLField(null=False, blank=False)
    type = models.ForeignKey('OrganizationType', on_delete=models.PROTECT, null=False, blank=False)
    size = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False, auto_now=True)

    def __str__(self) -> str:
        return self.name


# Accessible only to Super Admins
class OrganizationType(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title
    