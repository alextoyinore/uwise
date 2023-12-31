# Generated by Django 5.0 on 2023-12-31 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_user_is_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.SlugField(default='')),
                ('region', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='subscriptiontype',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('professional', 'Professional'), ('premium', 'Premium'), ('vocational', 'Vocational'), ('organization', 'Organization')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='details',
            field=models.SlugField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='academic_level',
            field=models.CharField(choices=[('degree', 'Degree'), ('masters', 'Masters'), ('undergraduate', 'Undergraduate'), ('doctorate', 'Doctorate'), ('highschool', 'High School'), ('other', 'Other')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
    ]
