# Generated by Django 5.0.1 on 2024-02-14 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0047_course_image_link_alter_course_skills'),
        ('orderAPI', '0004_order_amount_paid_order_transaction_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('user', 'course', 'transaction_id', 'transaction_reference')},
        ),
    ]