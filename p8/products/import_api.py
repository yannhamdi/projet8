""" module that import products from openfood api"""

import requests


def get_json():
    """method that look for products in the openfoodfact api"""
    url = 'https://fr.openfoodfacts.org/cgi/search.pl'
    params = {
               "action": "process",
               'tag_contains_0':"contains",
               'lang': "fr",
               "json": 1,
               "page_size": 1,
             }
    response = requests.get(url, params=params)
    print(response)
    products = []
    if response.status_code == 200:
        products = response.json()['products']



    return products