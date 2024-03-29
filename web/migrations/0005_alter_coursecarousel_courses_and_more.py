# Generated by Django 5.0.1 on 2024-02-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0029_alter_course_skills_alter_course_tags'),
        ('web', '0004_businessmodel_slug_footerlink_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecarousel',
            name='courses',
            field=models.ManyToManyField(related_name='course_carousel_courses', to='courseAPI.course', verbose_name='Courses'),
        ),
        migrations.AlterField(
            model_name='coursecarousel',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='coursecarousel',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Carousel Title'),
        ),
    ]
