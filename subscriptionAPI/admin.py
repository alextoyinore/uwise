from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_type')
    search_fields = ('user',)


@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'recurrent_type', 'active')
    search_fields = ('title',)


@admin.register(SubscriptionRecurrentType)
class SubscriptionRecurrentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_period', 'description', 'active')
    search_fields = ('title',)
