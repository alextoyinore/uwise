# Generated by Django 5.0.1 on 2024-02-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_footerlink_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
