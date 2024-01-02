from django.shortcuts import render

from . import serializers
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

class SubscriptionView(ModelViewSet):
    serializer_class = serializers.SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionTypeView(ModelViewSet):
    serializer_class = serializers.SubscriptionTypeSerializer
    queryset = SubscriptionType.objects.all()
    permission_classes = [IsAdminUser]


class SubscriptionRecurrentTypeView(ModelViewSet):
    serializer_class = serializers.SubscriptionRecurrentTypeSerializer
    queryset = SubscriptionRecurrentType.objects.all()
    permission_classes = [IsAdminUser]
