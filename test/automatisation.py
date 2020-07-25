from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 

class TestSelenium(LiveServerTestCase):      

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_login(self):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        binary = FirefoxBinary('/applications/firefox.app/contents/macOs/firefox-bin')
        driver = webdriver.Firefox(firefox_binary=binary,executable_path='/usr/local/bin/geckodriver', capabilities=cap)
        print("get")
        driver.get("http://127.0.0.1:8000/users/signin/" )
        print("user")
        username_input = driver.find_element_by_name("username")
        print("myuser")
        username_input.send_keys('myuser')
        print("password")
        password_input = driver.find_element_by_name("password")
        print("secret")
        password_input.send_keys('secret')
        print("click")
        driver.find_element_by_id("go").click()
        self.assertEqual(len(user), 1)