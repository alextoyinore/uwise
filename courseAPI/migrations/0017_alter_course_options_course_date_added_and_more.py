# Generated by Django 5.0.1 on 2024-02-02 09:11

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0016_course_courses'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-date_added', 'is_active', 'next_start_date', 'is_specialization')},
        ),
        migrations.AddField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='specialization_courses', to='courseAPI.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='facilitators',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
