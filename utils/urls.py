from django.urls import path
from .views import  *

# url patterns
urlpatterns = [
    # CATEGORIES

    path('categories', views=CategoryViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='categories'),
    path('category/<int:pk>', views=CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='category'),

    # TAGS

    path('tags', views=CategoryViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='tags'),
    path('tag/<int:pk>', views=CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='tag'),

    # LANGUAGES

    path('languages', views=LanguageViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='languages'),
    path('language/<int:pk>', views=LanguageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='language'),

    # COURSE LEVEL

    path('course-levels', views=CourseLevelViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='course-levels'),
    path('course-level/<int:pk>', views=CourseLevelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='course-level'),
]
