# Generated by Django 5.0.1 on 2024-03-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0054_alter_specializationcourse_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_link1',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_link2',
            field=models.URLField(blank=True, null=True),
        ),
    ]
