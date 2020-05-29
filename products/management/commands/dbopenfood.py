from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from products.models import Category, Products
from products.import_api import get_json


class Command(BaseCommand):
    """personnalized command"""
    help = "commands to fill up our database"


    def handle(self, *args, **options):
        """ funcion that will call all the methods to fill our database"""
        self.delete_all()
        for category in settings.FOOD_CATEGORIES:
            self.saving_cat(category)

    def saving_cat(self, category):
        """methods that fills the cat model"""
        self.category = category
        Category.objects.get_or_create(cat=category)
        self.db_product = get_json(category)
        
        i = 0
        while i <= ((len(self.db_product))-1):
            try:
                Products.objects.get_or_create(id_code=self.db_product[i]["code"],
                        food_name=self.db_product[i]["product_name"],
                        nutrition_grade=self.db_product[i]["nutrition_grade_fr"],
                                    food_link=self.db_product[i]["url"],
                             image_url=self.db_product[i]["image_url"])
                papa = (self.db_product[i]["categories"]).split(",")
                j = 0
                while j <= ((len(papa))-1):
                    pipi = ((papa[j]).lower())
                    p = pipi.strip()
                    if p[0] == " ":
                        p.replace(" ", "")
                        if p in settings.FOOD_CATEGORIES:
                            print(p)
                            Products.objects.get_or_create(category=p)
                            j = j + 1
                        j = j + 1
                    if p in settings.FOOD_CATEGORIES:
                        print(p)
                        Products.objects.get_or_create(category=p)
                        j= j + 1
                    j = j + 1
                i = i + 1
            except:
                i = i + 1
        
    def delete_all(self):
        Products.objects.all().delete()
        Category.objects.all().delete()