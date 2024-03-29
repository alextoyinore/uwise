# Generated by Django 5.0.1 on 2024-02-14 11:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseAPI', '0047_course_image_link_alter_course_skills'),
        ('orderAPI', '0003_alter_cart_course_alter_cart_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='abc123', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_reference',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='UserPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_course', to='courseAPI.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserPurchase',
                'verbose_name_plural': 'UserPurchases',
                'ordering': ('date_added',),
                'get_latest_by': 'date_added',
                'unique_together': {('user', 'course')},
            },
        ),
    ]
