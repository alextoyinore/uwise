from rest_framework.serializers import ModelSerializer
from .models import *
from .views import *


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionTypeSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'


class SubscriptionRecurrentTypeSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionRecurrentType
        fields = '__all__'

