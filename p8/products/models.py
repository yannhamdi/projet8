from django.db import models




class Category(models.Model):
    """we create the name for each categories"""
    cat = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.cat


class Products(models.Model):
    """ we class the model for each products"""
    id_code = models.BigIntegerField(primary_key=True)
    food_name = models.CharField(max_length=255)
    nutrition_grade = models.CharField(max_length=1)
    food_link = models.URLField(max_length=255)
    image_url = models.URLField(max_length=255)
    category = models.ManyToManyField("Category", related_name="products")
    def __str__(self):
        return self.food_name
