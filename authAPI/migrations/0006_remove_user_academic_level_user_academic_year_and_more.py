# Generated by Django 5.0.1 on 2024-01-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0005_remove_facilitator_user_ptr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='academic_level',
        ),
        migrations.AddField(
            model_name='user',
            name='academic_year',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
