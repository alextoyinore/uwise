# Generated by Django 5.0.1 on 2024-03-10 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0053_alter_specializationcourse_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specializationcourse',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
