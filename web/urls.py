from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomeView.as_view(), name='home'),
    path('about', view=AboutView.as_view(), name='about'),
    path('privacy', view=PrivacyView.as_view(), name='privacy'),
    path('contact', view=ContactView.as_view(), name='contact'),
    path('login', view=LoginView.as_view(), name='login'),
    path('signup', view=SignUpView.as_view(), name='signup'),
    path('course/<int:pk>', view=CourseView.as_view(), name='course'),
    path('course-list', view=CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/enroll', view=EnrollView.as_view(), name='enroll'),
]
