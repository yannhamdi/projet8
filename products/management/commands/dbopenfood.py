from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from products.models import Category, Products
from products.import_api import get_json


class Command(BaseCommand):
    """personnalized command"""
    help = "commands to fill up our database"


    def handle(self, *args, **options):
        """ funcion that will call all the methods to fill our database"""
        self.prod = get_json()
        self.saving_cat()
        self.create_product()
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
        while i <= (len(db_pro)-1):
            Products.objects.get_or_create(id_code=db_pro[i]["code"],
                                    food_name=db_pro[i]["product_name"],
                           nutrition_grade=db_pro[i]["nutrition_grade_fr"],
                                                 food_link=db_pro[i]["url"],
                                          image_url=db_pro[i]["image_url"])
            i = i+1
        
