from django.db import models
from django.conf import settings

from users.models import User 
from products.models import Products


class Favorite(models.Model):
    """class that create a model favoris that will connect the user's model and the products' model"""
    user_link = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_favoris")
    product_searched = models.ForeignKey("products.Products", on_delete=models.CASCADE, related_name="user_search")
    product_substitute = models.ForeignKey("products.Products", on_delete=models.CASCADE, related_name="product_substitute")

  