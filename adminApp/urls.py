# -*- coding: utf-8 -*-
from django.conf.urls import url
from adminApp.views import *

urlpatterns = [
    url(r'^$', admin_page),
    url(r'^admin/$', admin_page),
    url(r'delete/user/(\d+)$', delete_user),
    url(r'get_user_form/(\d+)$', get_user_form),
    url(r'create/user/(\d*)$', create_user),
]