# Generated by Django 5.0.1 on 2024-02-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilsAPI', '0016_alter_rating_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
