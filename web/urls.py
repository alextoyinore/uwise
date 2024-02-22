from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomeView.as_view(), name='home'),
    path('page/<str:page>', view=StaticPageView.as_view(), name='static'),
    # path('about', view=AboutView.as_view(), name='about'),
    # path('privacy', view=PrivacyView.as_view(), name='privacy'),
    # path('contact', view=ContactView.as_view(), name='contact'),
    path('login', view=LoginView.as_view(), name='login'),
    path('signup', view=SignUpView.as_view(), name='signup'),
    path('course/<int:pk>', view=CourseView.as_view(), name='course'),
    path('explore', view=ExploreView.as_view(), name='explore'),
    path('course/<int:pk>/enroll', view=EnrollView.as_view(), name='enroll'),
    path('user/logout', view=logout_user, name='logout-user'),
    path('dashboard', view=DashboardView.as_view(), name='dashboard'),
    path('learn/<int:pk>', view=LearnView.as_view(), name='learn'),
    path('learn/<int:pk>/<str:page>', view=LearnView.as_view(), name='learn'),
    path('me', view=ProfileView.as_view(), name='profile'),
    path('blogs', view=BlogsView.as_view(), name='blogs'),
    path('blog/<int:pk>', view=BlogView.as_view(), name='blog')
]

# handle404 = handle404
