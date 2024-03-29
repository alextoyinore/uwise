# Generated by Django 5.0.1 on 2024-01-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0013_course_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='specialization_courses', to='courseAPI.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_specialization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='next_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
