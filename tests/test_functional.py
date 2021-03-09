from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from selenium.webdriver.firefox.webdriver import WebDriver


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Firefox web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()
        super.tearDownClass()

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
