from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomeView.as_view()),
]
