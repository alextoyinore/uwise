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

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.course.title}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='order_course', null=False, blank=False)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    transaction_reference = models.CharField(max_length=200, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course', 'transaction_id', 'transaction_reference')
        ordering = ('date_added',)
        verbose_name_plural = 'Orders'
        get_latest_by = 'date_added'
        verbose_name = 'Order'

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.course.title}'


class UserPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_by_user', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchased_course', null=False, blank=False)
    is_completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')
        ordering = ('date_added',)
        verbose_name_plural = 'User Purchases'
        get_latest_by = 'date_added'
        verbose_name = 'User Purchase'

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.course.title}'
    
    