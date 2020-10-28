from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings

from products.models import Category, Products
from products.import_api import get_json


class Command(BaseCommand):
    """personnalized command"""
    help = "commands to fill up our database"

    def handle(self, *args, **options):
        """ funcion that will call all the methods to fill our database"""
        for category in settings.FOOD_CATEGORIES:
            self.saving_category(category)
        for category in settings.FOOD_CATEGORIES:
            self.saving_cat(category)
        with open("updatedb.log", "a") as logfile:
            logfile.write(f"Tâche cron effectuée à {datetime.now()}\n")
    def checking_blank(self, element):
        """ method that check blank lines"""
        keys = ["code", "product_name", "nutrition_grade_fr", "url",
                "image_url", "categories", "image_nutrition_url"]
        for key in keys:
            if key not in element or not element[key]:
                return False
        return True

    def saving_category(self, category):
        Category.objects.get_or_create(cat=category)

    def saving_cat(self, category):
        """methods that fills the cat model"""
        self.category = category
        self.db_product = get_json(category)
        for element in self.db_product:
            if self.checking_blank(element):
                try:
                    my_product = Products.objects.get(id_code=(element["code"]))
                except Products.DoesNotExist:
                    continue
                my_product.id_code = element.get("code")
                my_product.food_name = element.get("product_name")
                my_product.nutrition_grade = element.get("nutrition_grade_fr")
                my_product.food_link = element.get("url")
                my_product.image_url = element.get("image_url")
                my_product.image_nutrition_url = element.get("image_nutrition_url")
                my_product.save()
