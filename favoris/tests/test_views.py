from django.test import TestCase
from django.urls import reverse
from django.core.paginator import Paginator
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
        self.product_3, created = Products.objects.get_or_create(id_code=20930300, food_name="paysanne", nutrition_grade="e",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_3.category.add(s)
        self.product_4, created = Products.objects.get_or_create(id_code=20930392, food_name="calzone", nutrition_grade="a",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_4.category.add(s)
        self.product_5, created = Products.objects.get_or_create(id_code=20930391, food_name="orientale", nutrition_grade="e",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_5.category.add(s)
        self.product_6, created = Products.objects.get_or_create(id_code=20930398, food_name="thon", nutrition_grade="a",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_6.category.add(s)
        self.product_7, created = Products.objects.get_or_create(id_code=20930378, food_name="viande", nutrition_grade="d",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_7.category.add(s)
        self.product_8, created = Products.objects.get_or_create(id_code=20930353, food_name="poulet", nutrition_grade="a",
                                             image_url="www.deoeoli.fr", food_link="www.marguerite.fr")
        self.product_8.category.add(s)
        self.user_1 , created = User.objects.get_or_create(username="yann80", last_name="hamdi", first_name="yann", email= "hamdiyann@hotmail.com", password="ch171283")


    def test_response_post(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse('saving_search', args=[self.product_1.id_code, self.product_2.id_code]))
        self.assertEqual(response.status_code, 302)

    def test_display_account(self):
        # Create 13 search for pagination
        self.client.force_login(self.user_1)
        response = self.client.get(reverse('display_account'))
        fav_1, created = Favorite.objects.get_or_create(user_link=response.context.get('user'),product_searched=Products.objects.get(id_code=20930300), product_substitute=Products.objects.get(id_code=20930392))
        fav_2, created = Favorite.objects.get_or_create(user_link=response.context.get('user'),product_searched=Products.objects.get(id_code=20930391), product_substitute=Products.objects.get(id_code=20930398))
        fav_3, created =Favorite.objects.get_or_create(user_link=response.context.get('user'),product_searched=Products.objects.get(id_code=20930378), product_substitute=Products.objects.get(id_code=20930353))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue(response.context['page_obj'] == True)
        fa = Favorite.objects.all()
        print(fa)
        self.assertTrue(len(response.context['self.favoris_list']) == 4)
        response_2 = self.client.get(reverse('display_account')+'?page=2')
        self.assertEqual(response_2.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue(response_2.context['page_obj'] == True)
        self.assertTrue(len(response_2.context['self.favoris_list']) == 1)
   
