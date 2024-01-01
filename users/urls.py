from django.urls import path, re_path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

# urls
urlpatterns = [
    # LOGINS
    path('login/e', view=LoginWithEmailView.as_view(), name='email-login'),
    path('login/u', view=LoginWithUsernameView.as_view(), name='username-login'),
    path('login/<backend>', view=SocialLoginView.as_view({'post': 'create'}), name='social-login'),

    # LOGOUT
    path('logout', view=LogoutView.as_view({'post': 'create'}), name='logout'),

    # USER
    path('users/me', view=ProfileView.as_view({
        'get': 'retrieve'
    }), name='me'),
    path('users', view=UserView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='users'),
    path('user/<int:pk>', view=UserView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='user-detail'),

    # ACADEMIC LEVEL
    path('academic-level', view=AcademicLevelView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='academic-levels'),
    path('academic-level/<int:pk>', view=AcademicLevelView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='academic-level-detail'),

    # SUBSCRIPTION
    path('subscriptions', view=SubscriptionView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscriptions'),
    path('subscription/<int:pk>', view=SubscriptionView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscription-detail'),

    # SUBSCRIPTION TYPE
    path('subscription-types', view=SubscriptionTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscription-types'),
    path('subscription-type/<int:pk>', view=SubscriptionTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscription-type-detail'),

    # SUBSCRIPTION RECURRENT TYPE
    path('subscription-recurrent-types', view=SubscriptionRecurrentTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='subscription-recurrent-types'),
    path('subscription-recurrent-type/<int:pk>', view=SubscriptionRecurrentTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='subscription-recurrent-type-detail'),

    # ORGANIZATION
    path('organizations', view=OrganizationView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='organizations'),
    path('organization/<int:pk>', view=OrganizationView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='organization-detail'),

    # ORGANIZATION TYPE
    path('organization-types', view=OrganizationView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='organization-types'),
    path('organization-type/<int:pk>', view=OrganizationView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='organization-type-detail'),
]
