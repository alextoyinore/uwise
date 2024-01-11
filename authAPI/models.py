from django.db import models
from django.contrib.auth.models import AbstractUser
from authAPI.manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True, default='', blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    state = models.CharField(max_length=20, null=False, blank=False)
    marital_status = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.CharField(max_length=6, default='', blank=True)
    image = models.ImageField(upload_to='uploads/facilitators/', default='', null=True, blank=True)
    current_work_field = models.CharField(max_length=100, default='', blank=True)
    desired_work_field = models.CharField(max_length=100, default='', blank=True)
    current_job = models.CharField(max_length=100, default='', blank=True)
    desired_job = models.CharField(max_length=100, default='', blank=True)
    academic_level = models.CharField(max_length=50, default='', blank=True)

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
    registerer_name = models.CharField(max_length=150, null=False, blank=False)
    registerer_job_title = models.CharField(max_length=100, null=False, blank=False)
    registerer_age = models.IntegerField(null=False, blank=False)
    registerer_phone_number = models.CharField(max_length=15, null=False, blank=False)
    registerer_email = models.EmailField(null=False, blank=False)
    registerer_address = models.CharField(max_length=200, null=False, blank=False)
    registerer_country = models.CharField(max_length=200, null=False, blank=False)
    registerer_state = models.CharField(max_length=200, null=False, blank=False)
    registerer_city = models.CharField(max_length=200, null=False, blank=False)
    registerer_zip = models.CharField(max_length=200, null=False, blank=False)
    registerer_image = models.ImageField(default='', upload_to='')
    registerer_gender = models.CharField(max_length=200, null=False, blank=False)

    # ORGANIZATION DATA
    organization_name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(default='', upload_to='')
    location = models.CharField(max_length=100, default='', null=True, blank=True)
    website = models.URLField(null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    size = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False, auto_now=True)

    def __str__(self) -> str:
        return self.organization_name


class OrganizationUser(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=False, blank=True)
    job_title = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.user.get_full_name()} {self.organization.get_fields('organization_name')}'


# Accessible only to Super Admins
class OrganizationType(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(max_length=200, default='')

    def __str__(self) -> str:
        return self.title


class Facilitator(User):
    partner_organization = models.ForeignKey('PartnerOrganization',
                                             on_delete=models.SET_NULL,
                                             null=True, blank=True,
                                             related_name='partner_organization')

    def __str__(self):
        return self.get_full_name()


class PartnerOrganization(models.Model):
    contact_name = models.CharField(max_length=150, null=False, blank=False)
    contact_job_title = models.CharField(max_length=100, null=False, blank=False)
    contact_email = models.EmailField(null=False, blank=False)
    contact_phone = models.CharField(max_length=15, null=False, blank=False)
    contact_image = models.ImageField(default='', null=True, blank=True)
    partner_organization_name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.URLField(default='')
    location = models.CharField(max_length=100, default='', null=True, blank=True)
    website = models.URLField(null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    size = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False, auto_now=True)

    def __str__(self) -> str:
        return self.partner_organization_name
