from django.urls import path
from .views import *

# urls
urlpatterns = [
    # COURSE LEVEL

    path('course-levels', view=CourseLevelViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='course-levels'),
    path('course-level/<int:pk>', view=CourseLevelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='course-level'),
]
