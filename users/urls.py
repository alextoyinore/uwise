from django.urls import path, re_path
from .views import UserView, LoginView, ProfileView, SetUsername
from rest_framework.authtoken.views import obtain_auth_token

# urls
urlpatterns = [
    path('login', view=LoginView.as_view()),

    path('users/me', view=ProfileView.as_view({
        'get':'retrieve'
    })),

    path('users', view=UserView.as_view({
        'get':'list',
        'post':'create'
    }), name='users'),

    path('user/<int:pk>', view=UserView.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy'
    }), name='user-detail'),

    path('users/set_username', view=SetUsername.as_view({
        'patch':'partial_update'
    }))
]
