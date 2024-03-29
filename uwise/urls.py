"""
URL configuration for uwise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blogAPI/', include('blogAPI.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authAPI.urls')),
    path('api/v1/', include('courseAPI.urls')),
    path('api/v1/', include('subscriptionAPI.urls')),
    path('api/v1/', include('utilsAPI.urls')),
    path('api/v1/', include('orderAPI.urls')),
    path('api/v1/', include('blogAPI.urls')),
    path('', include('web.urls')),
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/', include('djoser.urls.authtoken')),
]

handle404 = web.views.handle404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

