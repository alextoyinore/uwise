from django.urls import path
from .views import *

urlpatterns = [
    # SUBSCRIPTION
    path('subscriptions', view=SubscriptionView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptions'),
    path('subscriptions/<int:pk>', view=SubscriptionView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscriptions-detail'),

    # SUBSCRIPTION TYPE
    path('subscriptions-types', view=SubscriptionTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptions-types'),
    path('subscriptions-type/<int:pk>', view=SubscriptionTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscriptions-type-detail'),

    # SUBSCRIPTION RECURRENT TYPE
    path('subscriptions-recurrent-types', view=SubscriptionRecurrentTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptions-recurrent-types'),
    path('subscriptions-recurrent-type/<int:pk>', view=SubscriptionRecurrentTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscriptions-recurrent-type-detail'),
]