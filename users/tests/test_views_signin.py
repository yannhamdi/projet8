from django.test import TestCase
from django.urls import reverse

from users.models import User 
from users.views import signin, signout, account, signup

class SignInViewsTest(TestCase):
    def test_signin(self):
        response = self.client.post(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_signout(self):
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)

    def test_account(self):
        response = self.client.post(reverse('account'))
        self.assertEqual(response.status_code, 200)
    
    