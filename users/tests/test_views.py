from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..models import User
from ..views import signup, signin, signout, account
from ..forms import SignUpForm


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'last_name': 'hamdi',
            'first_name': 'yann',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('search')

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
        response = self.client.post(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        response = self.client.post(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_signout(self):
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)

    def test_account(self):
        response = self.client.post(reverse('account'))
        self.assertEqual(response.status_code, 200)
    