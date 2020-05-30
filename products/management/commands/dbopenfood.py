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
            self.saving_category(category)
        for category in settings.FOOD_CATEGORIES:
            self.saving_cat(category)
    def checking_blank(self, element):
        """ method that check blank lines"""
        keys = ["code", "product_name", "nutrition_grade_fr", "url", "image_url", "categories"]
        for key in keys:
            if element[key]:
                return True
            return False

    def saving_category(self, category):
        Category.objects.get_or_create(cat=category)   

    def saving_cat(self, category):
        """methods that fills the cat model"""
        self.category = category
        
        self.db_product = get_json(category)
        for element in self.db_product:
            if self.checking_blank(element) is True:
                Products.objects.get_or_create(id_code=element["code"],
                        food_name=element["product_name"],
                        nutrition_grade=element["nutrition_grade_fr"],
                                    food_link=element["url"],
                             image_url=element["image_url"])
                papa = (element["categories"]).split(",")
                for item in papa:
                    p = (item.lower()).strip()
                    if p[0] == " ":
                        p.replace(" ", "")
                        if p in settings.FOOD_CATEGORIES:
                            r = Products.objects.get(id_code=element["code"])
                            s = Category.objects.get(cat=p)
                            r.category.add(s)
                            r.save()
                    if p in settings.FOOD_CATEGORIES:
                        r = Products.objects.get(id_code=element["code"])
                        s = Category.objects.get(cat=p)
                        r.category.add(s)
                        r.save()
    def delete_all(self):
        Products.objects.all().delete()
        Category.objects.all().delete()