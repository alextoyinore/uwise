# Generated by Django 5.0 on 2023-12-31 19:07

import django.db.models.deletion
import django.utils.timezone
import users.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('job_title', models.CharField(max_length=100)),
                ('organization_name', models.CharField(max_length=100)),
                ('logo', models.URLField(default='')),
                ('region', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('url', models.URLField()),
                ('work_email', models.EmailField(max_length=254)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionRecurrentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('postal_code', models.CharField(blank=True, default='', max_length=6)),
                ('current_job_field', models.CharField(blank=True, default='', max_length=100)),
                ('desired_job_field', models.CharField(blank=True, default='', max_length=100)),
                ('current_job', models.CharField(blank=True, default='', max_length=100)),
                ('desired_job', models.CharField(blank=True, default='', max_length=100)),
                ('is_student', models.BooleanField(default=False)),
                ('is_facilitator', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_subscriber', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('academic_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.academiclevel')),
                ('organization', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.organization')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.manager.CustomUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organizationtype'),
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.SlugField(max_length=1000)),
                ('active', models.BooleanField(default=False)),
                ('recurrent_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subscriptionrecurrenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_subscription', models.DateField()),
                ('subscription_renewal_date', models.DateField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subsciption_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.subscriptiontype')),
            ],
        ),
    ]
