from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


        products = [
            {"id": 1, "name": "Xiaomi Redmi Note 12"},
            {"id": 2, "name": "Samsung Galaxy S21"},
            {"id": 3, "name": "iPhone 12 Pro"},
            {"id": 4, "name": "Google Pixel 5"},
            {"id": 5, "name": "OnePlus 9 Pro"},
            {"id": 6, "name": "Xiaomi Mi 11"},
            {"id": 7, "name": "Samsung Galaxy A52"},
            {"id": 8, "name": "iPhone SE"},
            {"id": 9, "name": "Google Pixel 4a"},
            {"id": 10, "name": "OnePlus Nord"}
        ]


        sorted_products = sorted(products, key=lambda x: x["name"])


        grouped_products = {}
        for product in sorted_products:
            name = product['name']
            if name not in grouped_products:
                grouped_products[name] = []
            grouped_products[name].append(product)


        store_list = []
        for group_name, group_items in grouped_products.items():
            store_list.append({
                "id": group_items[0]["id"],
                "name": group_items[0]["name"]
            })


        store_dict = {
            "SOFTECH.KG": store_list
        }


        json_data = json.dumps(store_dict, indent=4)


        self.wfile.write(json_data.encode())


server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print('Сервер запущен на порту 8000...')
httpd.serve_forever()







