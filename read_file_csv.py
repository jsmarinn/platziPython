import csv

#leer un archivo

"""with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

# Mostrar la información por columnas
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")

new_product = {
    'name': "Wireless caharger",
    'price': 75,
    'quantity': 100,
    'brand': "CargerMaster",
    'category': "Accesories",
    'entry_date': '2025-07-01'
}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)
