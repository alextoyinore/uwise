# Generated by Django 5.0.1 on 2024-02-07 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0017_remove_organization_contact_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
    ]
