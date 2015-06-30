#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('accounts.views',
    url(r'^signin$', 'signin', name='signin'),
    url(r'^signout$', 'signout', name='signout'),
)
