from django.test import TestCase
from django.urls import reverse

from users.models import User 
from users.views import signin

class SignInViewsTest(TestCase):
    def test_signin(self):
        response = self.client.post(reverse('signin'))
        self.assertEqual(response.status_code, 200)