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

    # GENDER

    path('genders', view=GenderViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='genders'),
    path('gender/<int:pk>', view=GenderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='gender'),


    # GRADE

    path('grades', view=GradeViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='grades'),
    path('grade/<int:pk>', view=GradeViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='grade'),


    # MESSAGE

    path('messages', view=MessageViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='messages'),
    path('message/<int:pk>', view=MessageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='message'),

    # MESSAGE

    path('announcements', view=AnnouncementViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='announcements'),
    path('announcement/<int:pk>', view=AnnouncementViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='announcement'),


    # NOTE

    path('notes', view=GenderViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='notes'),
    path('note/<int:pk>', view=GenderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='note'),


    # RATING

    path('ratings', view=GenderViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='ratings'),
    path('rating/<int:pk>', view=GenderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='rating'),


    # REVIEW

    path('reviews', view=GenderViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='reviews'),
    path('review/<int:pk>', view=GenderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='review'),
]
