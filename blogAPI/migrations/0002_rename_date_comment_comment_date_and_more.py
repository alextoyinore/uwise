# Generated by Django 5.0.1 on 2024-01-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_comment',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='date_liked',
            new_name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
