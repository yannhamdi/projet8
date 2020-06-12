from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib import auth
from django import forms
from ..forms import SignUpForm, SignInForm
from ..models import User

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username','last_name', 'first_name', 'email','password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
    def test_form_signin_has_fields(self):
        form = SignInForm()
        expected = ['username', 'password']
        actual = list(form.fields)
        self.assertSequenceEqual(expected,actual)
    def test_clean_fake_password(self):
        test = SignInForm()
        user, created = User.objects.get_or_create(username="papa", last_name="sebti", first_name="zahia", email="hh@hotmail.com", password="123456789")
        username_entry = "papa"
        password_entry = "09876543"
        user = auth.authenticate(username=username_entry, password=password_entry)
        self.assertRaises(ValidationError)
    def test_clean_fake_username(self):
        test = SignInForm()
        user, created = User.objects.get_or_create(username="papa", last_name="sebti", first_name="zahia", email="hh@hotmail.com", password="123456789")
        username_entry = "maman"
        password_entry = "123456789"
        user = auth.authenticate(username=username_entry, password=password_entry)
        self.assertRaises(ValidationError)
        