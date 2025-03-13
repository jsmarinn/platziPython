import csv
import json

converts=[]
with open('products.csv', mode='r') as file:
    productos = csv.DictReader(file)
    for producto in productos:
        converts.append(producto)

with open('csv_2_json.json', mode='a+') as file:
        json.dump(converts, file, indent=4)