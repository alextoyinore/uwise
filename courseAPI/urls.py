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


    # COURSE

    path('courses', view=CourseViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='courses'),
    path('course/<int:pk>', view=CourseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='course'),


    # ANSWER

    path('answers', view=AnswerViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='answer'),
    path('answer/<int:pk>', view=AnswerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='answer'),


    # Audio

    path('audios', view=AudioViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='audios'),
    path('audio/<int:pk>', view=AudioViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='audio'),


    # FIELD

    path('fields', view=FieldViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='fields'),
    path('field/<int:pk>', view=FieldViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='field'),


    # IMAGE

    path('images', view=ImageViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='images'),
    path('image/<int:pk>', view=ImageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='image'),


    # MODULE

    path('lessons', view=LessonViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='lessons'),
    path('lesson/<int:pk>', view=LessonViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='lesson'),


    # QUESTION

    path('questions', view=QuestionViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='questions'),
    path('question/<int:pk>', view=QuestionViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='question'),


    # QUIZ

    path('quizzes', view=QuizViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='quizzes'),
    path('quiz/<int:pk>', view=QuizViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='quiz'),


    # READING

    path('readings', view=ReadingViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='readings'),
    path('reading/<int:pk>', view=ReadingViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='reading'),


    # VIDEO

    path('videos', view=VideoViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='videos'),
    path('video/<int:pk>', view=VideoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='video'),

    # SPECIALIZATION

    path('specializations', view=SpecializationViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='specializations'),
    path('specialization/<int:pk>', view=SpecializationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='specialization'),

    # SPECIALIZATION COURSES

    path('specialization-courses', view=SpecializationCourseViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='specialization-courses'),
    path('specialization-course/<int:pk>', view=SpecializationCourseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='specialization-course'),


    # USER COURSES

    path('user-courses', view=UserCourseViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='user-courses'),
    path('user-course/<int:pk>', view=UserCourseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='user-course'),


    # COURSE FACILITATOR

    path('course-facilitators', view=CourseFacilitatorViewSet.as_view({
        'post': 'create',
        'get': 'list'}), name='course-facilitators'),
    path('course-facilitator/<int:pk>', view=CourseFacilitatorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='course-facilitator'),
]
