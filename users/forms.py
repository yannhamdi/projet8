from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.exceptions import ValidationError
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')


class SignInForm(forms.Form):
    username = forms.CharField(label= "username", max_length=20)
    password = forms.CharField(label = "Mot-de-Passe", widget=forms.PasswordInput, min_length = 6, max_length= 16)
    def clean(self):
        """method that checks if the datas entered by the user match the database"""
        cleaned_data = super(SignInForm,self).clean()
        username_entry = cleaned_data.get("username")
        password_entry = cleaned_data.get("password")
        if username_entry and password_entry:
            user = auth.authenticate(username=username_entry, password=password_entry)
                 pass
             else:
                 raise forms.ValidationError("Vos identifiants sont érronés")
    


