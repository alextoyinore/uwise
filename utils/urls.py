from django.urls import path
from .views import  *

# url patterns
urlpatterns = [
    # CATEGORIES

    path('categories', view=CategoryViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='categories'),
    path('category/<int:pk>', view=CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='category'),

    # TAGS

    path('tags', view=CategoryViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='tags'),
    path('tag/<int:pk>', view=CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='tag'),

    # LANGUAGES

    path('languages', view=LanguageViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='languages'),
    path('language/<int:pk>', view=LanguageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='language'),
]
