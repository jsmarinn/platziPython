import json

with open('productos.json', mode='+r') as file:
    products = json.load(file)
    for product in products:
        print(product)
    for product in products:
        print(f"Product: {product['name']}, Price: {product['price']}")