from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', view=OrderViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ), name='orders'),

    path('orders/<int:pk>/', view=OrderViewSet.as_view(
        {'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'}
    ), name='order'),

    path('cart/', view=CartViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ), name='cart'),

    path('cart/<int:pk>/', view=CartViewSet.as_view(
        {'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'}
    ), name='cart')
]

