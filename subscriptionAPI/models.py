from django.db import models

import authAPI.models


# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(authAPI.models.User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    date_of_subscription = models.DateField()
    subscription_renewal_date = models.DateField()
    subscription_type = models.ForeignKey('SubscriptionType', on_delete=models.CASCADE, null=False, blank=False,
                                          default=None)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username


# Accessible to only Super Admins
class SubscriptionType(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, default='')
    recurrent_type = models.ForeignKey('SubscriptionRecurrentType', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_courses = models.IntegerField(default=1, null=False, blank=False)
    validity = models.TextField(max_length=200, editable=False, null=False, blank=False)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.validity = self.recurrent_type.time_period
        super(SubscriptionType, self).save()

    def __str__(self) -> str:
        return self.title


# Accessible to only Super Admins
class SubscriptionRecurrentType(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    time_period = models.BigIntegerField()
    description = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
