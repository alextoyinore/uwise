# Generated by Django 5.0.1 on 2024-02-02 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0014_course_courses_course_is_specialization_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courselevel',
            options={'ordering': ('-date',)},
        ),
        migrations.RemoveField(
            model_name='course',
            name='courses',
        ),
        migrations.CreateModel(
            name='CourseFacilitator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_facilitated', to='courseAPI.course')),
                ('facilitator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_facilitator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.RenameModel(
            old_name='Programme',
            new_name='Specialization',
        ),
        migrations.CreateModel(
            name='SpecializationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseAPI.course')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseAPI.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courseAPI.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
