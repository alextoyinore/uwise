# Generated by Django 5.0.1 on 2024-01-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='facilitator',
        ),
        migrations.RemoveField(
            model_name='course',
            name='organization',
        ),
        migrations.AddField(
            model_name='course',
            name='facilitator_username',
            field=models.CharField(default='toyin', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(max_length=200),
        ),
    ]
