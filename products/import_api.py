""" module that import products from openfood api"""

import requests


def get_json(category):
    """method that look for products in the openfoodfact api"""
    url = 'https://fr.openfoodfacts.org/cgi/search.pl'
    params = {
               "action": "process",
               "tagtype_0": "categories",
               "tag_contains_0": "contains",
               "tag_0": category,
               "json": 1,
               "page_size": 1000,
             }
    response = requests.get(url, params=params)
    products = []
    if response.status_code == 200:
        products = response.json()['products']
        return products
