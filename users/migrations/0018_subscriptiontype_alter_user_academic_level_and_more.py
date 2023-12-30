# Generated by Django 5.0 on 2023-12-30 23:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('student', 'Student'), ('professional', 'Professional'), ('premium', 'Premium')], default=None, max_length=100)),
                ('recurrent_type', models.CharField(choices=[('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly')], default=None, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.SlugField(max_length=5000)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='academic_level',
            field=models.CharField(choices=[('degree', 'Degree'), ('masters', 'Masters'), ('undergraduate', 'Undergraduate'), ('doctorate', 'Doctorate'), ('highschool', 'High School'), ('other', 'Other')], default=None, max_length=100),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_subscription', models.DateField()),
                ('subscription_renewal_date', models.DateField()),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('subsciption_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.subscriptiontype')),
            ],
        ),
    ]
