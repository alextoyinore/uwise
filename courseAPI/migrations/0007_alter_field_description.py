# Generated by Django 5.0.1 on 2024-01-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0006_alter_field_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
