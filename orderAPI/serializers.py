from rest_framework import serializers

from orderAPI.models import Order, Cart, UserPurchase


# Serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class UserPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPurchase
        fields = '__all__'
        