from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm

from .forms import SignUpForm, SignInForm
from users.models import User
from products.forms import ProductSearch


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
                nextt = request.GET.get('next', 'home')
                if nextt:
                    return redirect(nextt)
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
    form = ProductSearch(request.POST or None)
    return render(request, 'registration/account.html',
                  {'user_details': user_details, 'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'registration/password_changed.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
def password_changed(request):
    """views that confirms password changed"""
