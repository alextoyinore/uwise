# Generated by Django 5.0.1 on 2024-01-24 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0003_delete_gender_facilitator_bio_facilitator_field_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facilitator',
            options={'verbose_name': 'Facilitator'},
        ),
    ]
