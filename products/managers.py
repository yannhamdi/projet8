from django.db import models
from random import randint


class ProductManager(models.Manager):
    def search_products(self, search_entry):
        """the method will make a request to look for
        the product searched and the one to substitue"""
        returning_request_user = {}
        produ_id = None
        produ_id = self.filter(food_name__icontains=search_entry)
        category_product = produ_id[0].category.all()
        if produ_id and category_product:
            if len(category_product) > 1:
                cat = category_product[0]
                better_product = self.filter(category=cat).filter(
                    nutrition_grade__lt=produ_id[0].nutrition_grade)
                if better_product:
                    i = (len(better_product))-1
                    j = randint(0, i)
                    returning_request_user = {'product_searched':
                                      produ_id[0].id_code, 'substitue':
                                      better_product[j].id_code}
                return None
            cat = category_product[0]
            better_product = self.filter(category=cat).filter(
                nutrition_grade__lt=produ_id[0].nutrition_grade)
            if better_product:
                i = (len(better_product))-1
                j = randint(0, i)
                returning_request_user = {'product_searched':
                                      produ_id[0].id_code, 'substitue':
                                      better_product[j].id_code}
                return returning_request_user
            return None
        return None
