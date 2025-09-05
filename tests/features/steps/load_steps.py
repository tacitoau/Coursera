import json
import requests
from behave import * # pylint: disable=W0614

@given("the following products")
def step_impl(context):
    """ Load a product """
    headers = {\"Content-Type\": \"application/json\"}
    context.products = []
    for row in context.table:
        product = {
            "name": row["name"],
            "category": row["category"],
            "available": row["available"].lower() == "true",
            "price": float(row["price"])
        }
        context.products.append(product)
        create_url = context.base_url + \'/api/products\'
        response = requests.post(create_url, json=product, headers=headers)
        assert response.status_code == 201
