from django.db import models



class Category(models.Model):
    """we create the name for each categories"""
    cat = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.cat

class Cat_prod(models.Model):
    """we create an intermediary table in case one products has severals categories"""
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey("Products", on_delete=models.CASCADE, related_name="categories")


class Products(models.Model):
    """ we class the model for each products"""
    id_code = models.BigIntegerField(primary_key=True)
    food_name = models.CharField(max_length=255)
    nutrition_grade = models.CharField(max_length=1)
    food_link = models.URLField(max_length=255)
    def __str__(self):
        return self.food_name