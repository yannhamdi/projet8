from django.test import TestCase
from products.models import Category, Products


class TestProductsModel(TestCase):
    def test_product(self):
        category = Category.objects.create(cat="pizzas")
        self.assertEqual(category.cat, "pizzas")
        product = Products.objects.create(id_code=2344393, food_name="pizzas",nutrition_grade="a",image_url="www.oeoeieoirie.com"
                                            ,food_link="www.didjdijddj.com",image_nutrition_url="www.oeoeouou.fr")
        categ = Category.objects.get(cat=category.cat)
        product.category.add(categ)
        product.save()
        self.assertEqual(product.id_code, 2344393)
        self.assertEqual(product.food_name, "pizzas")
        self.assertEqual(product.nutrition_grade, "a")
        self.assertEqual(product.image_url, "www.oeoeieoirie.com")
        self.assertEqual(product.food_link, "www.didjdijddj.com")
        self.assertEqual(product.image_nutrition_url, "www.oeoeouou.fr")
        cate = product.category.all()
        cate2= str(cate[0])
        self.assertEqual(cate2, "pizzas")
        self.assertEqual(product.food_name, Products.__str__(product))
        self.assertEqual(category.cat, Category.__str__(category))