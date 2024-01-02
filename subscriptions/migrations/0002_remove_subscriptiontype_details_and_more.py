# Generated by Django 5.0 on 2024-01-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptiontype',
            name='details',
        ),
        migrations.AddField(
            model_name='subscriptiontype',
            name='number_of_courses',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='subscriptiontype',
            name='validity',
            field=models.TextField(default=30, editable=False, max_length=200),
            preserve_default=False,
        ),
    ]
