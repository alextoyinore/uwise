# Generated by Django 5.0.1 on 2024-02-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilsAPI', '0008_remove_message_title_remove_message_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
