# Generated by Django 5.0.1 on 2024-02-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0025_remove_answer_link_remove_audio_link_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-date_created', 'is_active', 'next_start_date')},
        ),
        migrations.RemoveField(
            model_name='course',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='course',
            name='facilitators',
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_specialization',
        ),
        migrations.RemoveField(
            model_name='course',
            name='lessons',
        ),
        migrations.RemoveField(
            model_name='field',
            name='link',
        ),
        migrations.RemoveField(
            model_name='specialization',
            name='link',
        ),
        migrations.RemoveField(
            model_name='specializationcourse',
            name='link',
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/courses/'),
        ),
    ]
