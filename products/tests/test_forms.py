from django.test import TestCase
from ..forms import ProductSearch



class SearchForm(TestCase):
    def test_form_search(self):
        form = ProductSearch()
        expected = ['search']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)