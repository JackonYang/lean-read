#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib import messages
from django.contrib import auth


def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, u'username or password error.')

    return render_to_response('signin.html', RequestContext(request))


def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
