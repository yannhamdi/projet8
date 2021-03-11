from django.test import LiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
from selenium import webdriver
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.core import mail

browser= webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class CustomerTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = Firefox()
        cls.browser.implicitly_wait(50)
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()


    def setUp(self):
        User = get_user_model()
        self.password = "affdLhj23HJ"
        self.email = "testuser@test.com"
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="affdLhj23HJ",
        )

    def test_login(self):
        self.browser.get(self.live_server_url + reverse('signin'))
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys(self.password)
        button = self.browser.find_element_by_id("go")
        button.click()
        logout_button = self.browser.find_element_by_css_selector(
            f"a[href=\"{reverse('signout')}\"]"
        )
        self.assertTrue(logout_button.is_displayed)

    def test_reset_password(self):
        """ test reset password"""
        self.browser.get(self.live_server_url + reverse('password_reset'))
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys(self.email)
        button = self.browser.find_element_by_id("button-send-reset")
        button.click()
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Réinitialisation du mot de passe", mail.outbox[0].subject)


