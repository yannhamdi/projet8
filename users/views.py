from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            auth.login(request, user)
            return redirect('search')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})