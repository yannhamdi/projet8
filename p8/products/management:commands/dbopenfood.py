from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from products.models import Category, Cat_prod, Prducts
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
        i= 0
        popo = self.prod[i]["categories"]
        papa=popo.split(",")
        while i < len(papa)-1 :
            c = Category.objects.get_or_create(cat = papa[i])
            c.save()
            i = i+1
