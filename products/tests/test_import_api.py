
from django.test import TestCase
from unittest.mock import patch, MagicMock
from products.import_api import get_json
import requests

class TestImportApi(TestCase):
    @patch('requests.get')
    def test_get_json(self,mockget_json):
        category = "pizzas"
        mockget_json.return_value.json.return_value ={
        "products": [
          { "code": 122233,
                "product_name": "pizzas",
                "nutrition_grade_fr": "a",
                "url": "www.dkdjkdjd.com",
                "image_url": "www.image.fr"


              }]
              }
        mockget_json.return_value.status_code = 200
        prod = get_json(category)
        self.assertEqual(len(prod),1)
          