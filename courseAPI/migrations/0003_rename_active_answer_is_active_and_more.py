# Generated by Django 5.0.1 on 2024-01-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0002_remove_course_facilitator_remove_course_organization_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='facilitator_username',
            new_name='facilitator',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='field',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='reading',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='specialization',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='specializationcourse',
            old_name='active',
            new_name='is_active',
        ),
        migrations.AddField(
            model_name='audio',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='courselevel',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='courselevel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='image',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='module',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
