from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomeView.as_view(), name='home'),
    path('about', view=AboutView.as_view(), name='about'),
    path('privacy', view=PrivacyView.as_view(), name='privacy'),
    path('contact', view=ContactView.as_view(), name='contact'),
    path('<str:page>', view=PageView.as_view(), name='page'),
    path('auth', view=AuthView.as_view(), name='auth'),
]
