# Generated by Django 5.0.1 on 2024-02-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0019_lesson_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-date_created', 'is_active', 'next_start_date', 'is_specialization')},
        ),
        migrations.RemoveField(
            model_name='course',
            name='date_added',
        ),
        migrations.AddField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
