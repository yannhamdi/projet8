from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.core.exceptions import ValidationError
from django.contrib import auth
from django.shortcuts import render, redirect
from django.conf import settings
from django import forms

from .forms import SignUpForm, SignInForm
from users.models import User

def signup(request):
    """views that allows the user to signup"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



def signin(request):
    """view that connect the user"""
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('/products/home/?next=%s' % request.path)
            
    else:
        form = SignInForm()
    return render(request, 'registration/signin.html', {"form": form})

def signout(request):
    """views that logs out"""
    auth.logout(request)
    return redirect('home')

def account(request):
    """ views that display user's details"""
    user_details = User(request)
    return render(request, 'registration/account.html', {'user_details': user_details})



