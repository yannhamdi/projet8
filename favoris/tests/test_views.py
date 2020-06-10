from django.test import TestCase
from django.urls import reverse

from favoris.models import Favorite
from products.models import Category, Products
from users.models import User

class FavoriteView(TestCase):

    def test_view_saving_search(self):
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
        produ_id = Products.objects.filter(food_name__icontains="reine")
        user_1 , created = User.objects.get_or_create(username="yann80", last_name="hamdi", first_name="yann", email= "hamdiyann@hotmail.com", password="ch171283")
        favoris, created = Favorite.objects.get_or_create(user_link=user_1, product_searched=product_1, product_substitute=product_2)
        response = self.client.get(reverse('saving_search', args=[product_1.id_code, product_2.id_code]))
        self.assertEqual(favoris.user_link, user_1)
        self.assertEqual(favoris.product_searched, product_1)
        self.assertEqual(favoris.product_substitute, product_2)
        self.assertEqual(response.status_code, 302)
   
