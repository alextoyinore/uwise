# Generated by Django 5.0.1 on 2024-02-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0028_alter_audio_audio_alter_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]