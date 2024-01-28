from django.urls import path, re_path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

# urls
urlpatterns = [
    # LOGINS
    path('login/e', view=LoginWithEmailView.as_view(), name='email-login'),
    path('login/u', view=LoginWithUsernameView.as_view(), name='username-login'),
    path('login/<backend>', view=SocialLoginView.as_view({'post': 'create'}), name='social-login'),

    # REFERRAL
    path('referrals/', view=ReferralView.as_view({
        'get': 'list', 'post': 'create'
    }), name='referrals'),
    path('referral/', view=ReferralView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='referral'),

    # LOGOUT
    path('logout', view=LogoutView.as_view({'post': 'create'}), name='logout'),

    # USER
    path('users/me', view=ProfileView.as_view({
        'get': 'retrieve'
    }), name='me'),
    path('users', view=UserView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='authAPI'),
    path('user/<int:pk>', view=UserView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='user'),

    # ACADEMIC LEVEL
    path('academic-levels', view=AcademicLevelView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='academic-levels'),
    path('academic-level/<int:pk>', view=AcademicLevelView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='academic-level'),

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
    path('organization-types', view=OrganizationTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='organization-types'),
    path('organization-type/<int:pk>', view=OrganizationTypeView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='organization-type-detail'),
]
