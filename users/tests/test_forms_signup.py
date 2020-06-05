from django.test import TestCase
from ..forms import SignUpForm
from ..models import User

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username','name', 'first_name', 'email','password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)