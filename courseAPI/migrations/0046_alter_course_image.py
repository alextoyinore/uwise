# Generated by Django 5.0.1 on 2024-02-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0045_remove_course_facilitators_class_facilitator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses'),
        ),
    ]
