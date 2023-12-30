from django.urls import path, re_path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

# urls
urlpatterns = [
    # LOGINS
    path('login/e', view=LoginWithEmailView.as_view(), name='email-login'),
    path('login/u', view=LoginWithUsernameView.as_view(), name='username-login'),
    path('login/<backend>', view=SocialLoginView.as_view({'post':'create'}), name='social-login'),

    # USER
    path('users/me', view=ProfileView.as_view({
        'get':'retrieve'
    }), name='me'),
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

    #LOGOUT
    path('logout', view=LogoutView.as_view(), name='logout')
]



