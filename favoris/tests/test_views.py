from django.test import TestCase
from django.urls import reverse

from favoris.models import Favorite
from products.models import Category, Products
from users.models import User

class FavoriteView(TestCase):

    def setUp(self):
        self.category = Category.objects.get_or_create(cat= "pizzas")
        self.product_1, created = Products.objects.get_or_create(id_code=20930393, food_name="reine", nutrition_grade="c",
        	                                 image_url="www.deoeoei.fr", food_link="www.reine.fr")
        s = Category.objects.get(cat="pizzas")
        self.product_1.category.add(s)
        self.product_1.save()
        self.product_2, created = Products.objects.get_or_create(id_code=20930395, food_name="marguerite", nutrition_grade="a",
        	                                 image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_2.category.add(s)
        self.product_2.save()
        self.user_1 , created = User.objects.get_or_create(username="yann80", last_name="hamdi", first_name="yann", email= "hamdiyann@hotmail.com", password="ch171283")


    def test_response_post(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse('saving_search', args=[self.product_1.id_code, self.product_2.id_code]))
        self.assertEqual(response.status_code, 302)
   
