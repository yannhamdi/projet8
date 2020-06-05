from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import SignUpForm, SignInForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('search')
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
                return redirect('/products/search/?next=%s' % request.path)
            print("erreur")
    else:
        form = SignInForm()
    return render(request, 'registration/signin.html', {'form': form})