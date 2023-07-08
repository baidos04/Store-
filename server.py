import requests

API_URL = "https://test-docs.stores.kg/api/products"
API_TOKEN = "00e82b9c923ba5851821bc8215004d26"

def make_api_request():
    headers = {
        "api-token": API_TOKEN,
    }

    params = {
        "page": 1,
        "itemsPerPage": 30,
        "order[price]": "asc",
        "order[name]": "asc"
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()

        if "hydra:member" in data:
            products = data["hydra:member"]
            process_products(products)
        else:
            print("Отсутствуют продукты в ответе API.")

    except requests.exceptions.RequestException as e:
        print("Ошибка при выполнении запроса:", str(e))

def process_products(products):
    for product in products:
        product_id = product["id"]
        product_name = product["name"]
        print(f"Product ID: {product_id}, Name: {product_name}")

make_api_request()



















