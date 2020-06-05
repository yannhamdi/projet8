from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')


class SignInForm(forms.Form):
    username = forms.CharField(label= "username", max_length=20)
    password = forms.CharField(label = "Mot-de-Passe", widget=forms.PasswordInput, min_length = 6, max_length= 16)
