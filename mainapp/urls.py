# -*- coding: utf-8 -*-
"""f URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    # url(r'^admin/', include('adminApp.urls')),

    url(r'^$', index, name='index'),
    url(r'^locks/$', locks, name='locks'),
    url(r'^haircut/$', haircut, name='haircut'),
    url(r'^color/$', color, name='color'),
    url(r'^hairdress/$', hairdress, name='hairdress'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^service/$', s_wow, name='s_wow'),
    url(r'^contacts/$', contacts, name='contacts'),

    url(r'^user/', include('userManagementApp.urls')),
    # url(r'^admin/', include('adminApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
