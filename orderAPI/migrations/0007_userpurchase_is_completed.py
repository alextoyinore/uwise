# Generated by Django 5.0.1 on 2024-03-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderAPI', '0006_alter_userpurchase_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpurchase',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
