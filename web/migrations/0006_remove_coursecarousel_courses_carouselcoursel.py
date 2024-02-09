# Generated by Django 5.0.1 on 2024-02-03 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0029_alter_course_skills_alter_course_tags'),
        ('web', '0005_alter_coursecarousel_courses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecarousel',
            name='courses',
        ),
        migrations.CreateModel(
            name='CarouselCoursel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.coursecarousel', verbose_name='Carousel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseAPI.course', verbose_name='Course')),
            ],
        ),
    ]