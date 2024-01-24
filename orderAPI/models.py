from django.db import models

from authAPI.models import User
from courseAPI.models import Course


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cart_course', null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')
        ordering = ('date_added',)
        verbose_name_plural = 'Carts'
        get_latest_by = 'date_added'
        verbose_name = 'Cart'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='order_course', null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')
        ordering = ('date_added',)
        verbose_name_plural = 'Orders'
        get_latest_by = 'date_added'
        verbose_name = 'Order'
