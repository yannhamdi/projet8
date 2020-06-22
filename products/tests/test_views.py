from django.test import TestCase
from django.urls import reverse
from products.forms import ProductSearch
from products.views import display, lire, search
from products.models import Category, Products
from random import randint

class ProductsView(TestCase):
    def setUp(self):
        self.category = Category.objects.get_or_create(cat= "pizzas")
        self.product_1, created = Products.objects.get_or_create(id_code=20930393, food_name="reine", nutrition_grade="c",
                                image_url="www.deoeoei.fr", food_link="www.reine.fr", image_nutrition_url="www.oeoeouou.fr")
        s = Category.objects.get(cat="pizzas")
        self.product_1.category.add(s)
        self.product_1.save()
        self.product_2, created = Products.objects.get_or_create(id_code=20930395, food_name="marguerite", nutrition_grade="a",
                                image_url="www.deoeoli.fr", food_link="www.marguerite.fr", image_nutrition_url="www.oeoeouou.fr")
        self.product_2.category.add(s)
        self.product_2.save()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_search(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
    def test_search_with_post(self):
        response_1 = self.client.post(reverse('search'), {'search': 'reine'} )
        self.assertEqual(response_1.status_code, 302)
    def test_lire(self):
        response = self.client.post(reverse('lire', args=[20930395]))
        self.assertEqual(response.status_code, 200)
    
    def test_lire_error(self):
        response = self.client.post(reverse('lire', args=[2093]))
        self.assertEqual(response.status_code, 404)
    

    
    def test_display(self):
        id_searched = 20930393
        id_substitue = 20930395
        response = self.client.get(reverse('display', args=[id_searched, id_substitue]))
        self.assertEqual(response.status_code, 200)






