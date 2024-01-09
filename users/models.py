from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.OneToOneField('UserGender', default=None, on_delete=models.CASCADE, null=True, blank=False, related_name='user_gender')
    username = models.CharField(max_length=100, unique=True, default='', blank=False)
    country = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.CharField(max_length=6, default='', blank=True)
    image = models.URLField(default=''),
    current_job_field = models.CharField(max_length=100, default='', blank=True)
    desired_job_field = models.CharField(max_length=100, default='', blank=True)
    current_job = models.CharField(max_length=100, default='', blank=True)
    desired_job = models.CharField(max_length=100, default='', blank=True)
    academic_level = models.OneToOneField('UserAcademicLevel', default=None, on_delete=models.CASCADE, null=True, blank=True, related_name='user_academic_level')
    organization = models.ForeignKey('Organization', default=None, null=True, on_delete=models.CASCADE)

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
class Gender(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, default=None, blank=False)

    def __str__(self) -> str:
        return self.title


class UserGender(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> User:
        return self.user


# Accessible only to Super Admins
class AcademicLevel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title


class UserAcademicLevel(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)
    academic_level = models.ForeignKey('AcademicLevel', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> User:
        return self.user


class Organization(models.Model):
    fullname = models.CharField(max_length=150, null=False, blank=False)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    organization_name = models.CharField(max_length=100, null=False, blank=False)
    image = models.URLField(default='')
    region = models.CharField(max_length=100, default='', null=True, blank=True)
    url = models.URLField(null=False, blank=False)
    work_email = models.EmailField(unique=True, null=False, blank=False)
    type = models.ForeignKey('OrganizationType', on_delete=models.CASCADE, null=False, blank=False)
    size = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return self.organization_name


# Accessible only to Super Admins
class OrganizationType(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title
