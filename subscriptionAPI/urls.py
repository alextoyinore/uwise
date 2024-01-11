from django.urls import path
from .views import *

urlpatterns = [
    # SUBSCRIPTION
    path('subscriptionAPI', view=SubscriptionView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptionAPI'),
    path('subscriptionAPI/<int:pk>', view=SubscriptionView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscriptionAPI-detail'),

    # SUBSCRIPTION TYPE
    path('subscriptionAPI-types', view=SubscriptionTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptionAPI-types'),
    path('subscriptionAPI-type/<int:pk>', view=SubscriptionTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscriptionAPI-type-detail'),

    # SUBSCRIPTION RECURRENT TYPE
    path('subscriptionAPI-recurrent-types', view=SubscriptionRecurrentTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptionAPI-recurrent-types'),
    path('subscriptionAPI-recurrent-type/<int:pk>', view=SubscriptionRecurrentTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscriptionAPI-recurrent-type-detail'),
]