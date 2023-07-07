import requests
import json

API_URL = "https://test-docs.stores.kg/api"
API_TOKEN = "api-token: 00e82b9c923ba5851821bc8215004d26"

SOFTECH = [
    {"name": "Xiaomi Redmi Note 10", "id": 1},
    {"name": "Samsung Galaxy S21", "id": 2},
    {"name": "iPhone 12 Pro", "id": 3},
]

def make_api_request():
    headers = {
        "api-token": API_TOKEN,
    }

    for phone in SOFTECH:
        params = {
            "page": 1,
            "itemsPerPage": 30,
            "order[price]": "asc",
            "name": phone["name"],
            "point.id": phone["id"]
        }

        try:
            response = requests.get(API_URL, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()

            if "hydra:member" in data:
                products = data["hydra:member"]
                sorted_products = sort_products_by_name(products)
                process_products(sorted_products)
            else:
                print("Отсутствуют продукты в ответе API.")

        except requests.exceptions.RequestException as e:
            print("Ошибка при выполнении запроса:", str(e))

def sort_products_by_name(products):
    sorted_products = sorted(products, key=lambda p: p["name"])
    return sorted_products

def process_products(products):
    json_data = json.dumps(products, indent=4)
    print(json_data)


make_api_request()

















