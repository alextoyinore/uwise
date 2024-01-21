from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomeView.as_view(), name='home'),
    path('about', view=AboutView.as_view(), name='about'),
    path('privacy', view=PrivacyView.as_view(), name='privacy'),
    path('contact', view=ContactView.as_view(), name='contact'),
    path('login', view=LoginView.as_view(), name='login'),
    path('signup', view=SignUpView.as_view(), name='signup'),
]
