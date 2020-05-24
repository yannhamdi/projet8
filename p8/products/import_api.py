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
        popo = products[1]["categories"]
        papa=popo.split(",")
        i = 0
        while i < len(papa)-1 :
            print(papa[i])
            i = i+1





    
    return products
get_json()