from django.test import TestCase
from favoris.models import Favorite
from users.models import User
from products.models import Category, Products



class TestFavoriteModel(TestCase):
    def test_favorite_model(self):
        category = Category.objects.get_or_create(cat= "pizzas")
        product_1, created = Products.objects.get_or_create(id_code=20930393, food_name="reine", nutrition_grade="c",
                                             image_url="www.deoeoei.fr", food_link="www.reine.fr")
        s = Category.objects.get(cat="pizzas")
        product_1.category.add(s)
        product_1.save()
        product_2, created = Products.objects.get_or_create(id_code=20930395, food_name="marguerite", nutrition_grade="a",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        product_2.category.add(s)
        product_2.save()
        user_1 , created = User.objects.get_or_create(username="yann80", last_name="hamdi", first_name="yann", email= "hamdiyann@hotmail.com", password="ch171283")
        favoris, created = Favorite.objects.get_or_create(user_link=user_1, product_searched=product_1, product_substitute=product_2)
        self.assertEqual(favoris.user_link, user_1)
        self.assertEqual(favoris.product_searched, product_1)
        self.assertEqual(favoris.product_substitute, product_2)




from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

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
        self.selenium.get('%s%s' % (self.live_server_url, '/signin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.assertEqual(True, True)