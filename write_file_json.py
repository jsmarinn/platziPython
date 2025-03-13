import json

new_product = {
        "name": "airPods",
        "price": 199,
        "quantity": 56120,
        "brand": "TApple",
        "category": "Accessories",
        "entry_date": "2025-03-10"
}

with open('productos.json', mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open('productos.json', mode='w') as file:
    json.dump(products, file, indent=4)