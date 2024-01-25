from django.urls import path
from .views import *

urlpatterns = [
    path('posts', view=PostViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ), name='posts'),

    path('post/<int:pk>', view=PostViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'
    }), name='post'),

    path('comments', view=CommentViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ), name='comments'),

    path('comment/<int:pk>', view=CommentViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'
    }), name='comment'),

    path('like', view=LikeViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ), name='likes'),

    path('like/<int:pk>', view=LikeViewSet.as_view(
        {'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'}
    ), name='like'),
]

