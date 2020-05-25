from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from products.models import Category, Cat_prod, Products
from products.import_api import get_json


class Command(BaseCommand):
    """personnalized command"""
    help = "commands to fill up our database"


    def handle(self, *args, **options):
        """ funcion that will call all the methods to fill our database"""
        self.prod = get_json()
        self.saving_cat()

    def saving_cat(self):
        """methods that fills the cat model"""
        popo = self.prod
        i = 0
        while i <= ((len(popo))-1):
            papa = (popo[i]["categories"]).split(',')
            j = 0
            while j <= ((len(papa))-1):
                c = Category.objects.get_or_create(cat=papa[j])
                i = i+1
                j = j+1
        

    def create_product(self):
        """methods that fills up our model product"""
        db_pro = self.prod
        i = 0
        while i <= (len(products)-1):
            Products.objects.get_or_create(id_code=products[i]["code"],
                                    food_name=products[i]["product_name"],
                           nutrition_grade=products[i]["nutrition_grade_fr"],
                                                 food_link=products[i]["url"],
                                          image_url=products[i]["image_url"])
            i = i+1
        
