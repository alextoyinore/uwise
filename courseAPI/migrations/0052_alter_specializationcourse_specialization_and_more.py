# Generated by Django 5.0.1 on 2024-03-10 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0051_specialization_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specializationcourse',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialization', to='courseAPI.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_specialization',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='specializationcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialization_course', to='courseAPI.course'),
        ),
        migrations.DeleteModel(
            name='Specialization',
        ),
    ]