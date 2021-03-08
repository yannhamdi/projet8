from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase, Client, RequestFactory
from ..models import User
from ..views import signup, signin, signout, account, change_password
from ..forms import SignUpForm, SignInForm


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'last_name': 'hamdi',
            'first_name': 'yann',
            'email': 'ham@homtmail.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')
        
    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

    
    
    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_signin_post(self):
        url = reverse('signin')
        data = {
             'username': 'john',
             'password': 'abcdef123456'
        }
        self.response_2 = self.client.post(url, data)
        self.assertEqual(self.response_2.status_code, 302)

    
    def test_signout(self):
        response = self.client.get(reverse('signout'))
        self.assertEqual(self.response.status_code, 302)



        self.assertEqual(response.status_code, 302)

    def test_account(self):
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)

    def test_correct_password(self):
        data = {
            'username': 'john',
            'last_name': 'hamdi',
            'first_name': 'yann',
            'email': 'ham@homtmail.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456',
           }         
        data2 = {
        'new_password1': 'abc123',
        'new_password2': 'abc123',
        }
        form = PasswordChangeForm(data, data2)
        self.response_3 = self.client.post(reverse('change_password'))
        self.assertFalse(form.is_valid())
        messages = list(self.response_3.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Please correct the error below.')
    
    