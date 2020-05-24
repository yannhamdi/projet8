from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from products.models import Category, Cat_prod, Prducts
from products.import_api import get_json