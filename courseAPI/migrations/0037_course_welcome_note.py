# Generated by Django 5.0.1 on 2024-02-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0036_alter_facilitatorattendance_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='welcome_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]