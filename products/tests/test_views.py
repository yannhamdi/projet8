from django.test import TestCase
from django.urls import reverse

from products.views import display, lire, search

class SignInViewsTest(TestCase):

    def test_search(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    def test_lire_error(self):
        response = self.client.post(reverse('lire', args=[99898]))
        self.assertEqual(response.status_code, 404)