from django.shortcuts import render, render_to_response
from django.contrib import auth
from login_demo_app.models import UserProfile
from django.http import HttpResponseRedirect

def login(request):
    return render_to_response("demo/login.html",{"user":request.user})

def logged(request):
    return render_to_response("demo/logged.html",{"user":request.user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")
