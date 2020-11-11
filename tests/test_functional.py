from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from users.models import User

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class TestSelenium(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(firefox_options=firefox_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.selenium.quit()

    def setUp(self):
        self.password = "affdLhj23HJ"
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="affdLhj23HJ",
        )

    def test_login(self):
        self.selenium.get(self.live_server_url + reverse('signin'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.password)
        button = self.selenium.find_element_by_id("go")
        button.click()
        logout_button = self.selenium.find_element_by_css_selector(
            f"a[href=\"{reverse('signout')}\"]"
        )
        self.assertTrue(logout_button.is_displayed)
