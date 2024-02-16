from django.contrib import admin

from orderAPI.models import Cart, Order, UserPurchase


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date_added')
    search_fields = ('user', 'course')
    date_hierarchy = 'date_added'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date_added')
    search_fields = ('user', 'course')
    date_hierarchy = 'date_added'


@admin.register(UserPurchase)
class UserPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date_added')
    search_fields = ('user', 'course')
    date_hierarchy = 'date_added'

