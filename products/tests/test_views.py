from django.test import TestCase
from django.urls import reverse

from products.views import display, lire, search
from products.models import Category, Products
from random import randint

class ProductsView(TestCase):

    def test_search(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    def test_lire_error(self):
        response = self.client.post(reverse('lire', args=[99898]))
        self.assertEqual(response.status_code, 404)
    
    def test_product_search(self):
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
        category_product = produ_id[0].category.all()
        cat = category_product[0]
        better_product = Products.objects.filter(category=cat).filter(nutrition_grade__lt=produ_id[0].nutrition_grade)
        i=(len(better_product))-1
        j=randint(0,i)
        cat = category_product[0]
        better_product = Products.objects.filter(category=cat).filter(nutrition_grade__lt=produ_id[0].nutrition_grade)
        better = better_product[0].food_name
        prod_2 = product_2.food_name
        prod_1= product_1.food_name
        prod_id = produ_id[0].food_name
        response =self.client.get(reverse('display', args=[int(produ_id[0].id_code), int(better_product[j].id_code)]))
        self.assertEqual(prod_1, prod_id)
        self.assertEqual(prod_2, better)
        self.assertEqual(response.status_code, 200)






