# Generated by Django 5.0.1 on 2024-02-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courseAPI', '0027_alter_audio_audio_alter_course_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('url_name', models.CharField(max_length=200, verbose_name='url_name')),
                ('description', models.TextField(verbose_name='description')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='CourseCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='course_carousel')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('courses', models.ManyToManyField(related_name='course_carousel_courses', to='courseAPI.course', verbose_name='courses')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
