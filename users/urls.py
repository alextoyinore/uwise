from django.urls import path, re_path
from .views import UserView, LoginWithEmailView, LoginWithUsernameView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token

# urls
urlpatterns = [
    # LOGINS
    path('login/e', view=LoginWithEmailView.as_view()),
    path('login/u', view=LoginWithUsernameView.as_view()),

    # USER
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
]

