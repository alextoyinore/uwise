# Generated by Django 5.0.1 on 2024-02-07 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0023_user_organization_alter_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_contact', to=settings.AUTH_USER_MODEL),
        ),
    ]
