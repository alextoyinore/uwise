# Generated by Django 5.0.1 on 2024-02-04 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0033_alter_lesson_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='time_duration',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]