
import csv

class Vehiculo:
    def __init__(self, marca, linea, precio):
        self.marca = marca
        self.linea = linea
        self.precio = precio
        self.es_disponible = True

    def get_marca(self):
        return self.marca
    
    def get_linea(self):
        return self.linea
    
    def get_precio(self):
        return self.precio
    
    def get_disponibilidad(self):
        return self.es_disponible
    
    def set_disponibilidad(self, disponibilidad):
        self.es_disponible = disponibilidad
    
    def encender(self):
        raise NotImplementedError("Este método no se ha implementado")
    
    def apagar(self):
        raise NotImplementedError("Este método no se ha implementado")
    
    def __str__(self):
        return {'marca': self.marca,
                'linea': self.linea,
                'precio': self.precio
        }
    
class Carro(Vehiculo):
    def encender(self):
        if self.get_disponibilidad():
            print(f"El motor del carro {self.get_marca()} se ha encendido.")
        else:
            print(f"El carro {self.get_marca()} no se encuentra disponible.")

class Bicicleta(Vehiculo):
    def encender(self):
        if self.get_disponibilidad():
            print(f"Bicicleta {self.get_marca()} en movimiento.")
        else:
            print(f"Bicicleta {self.get_marca()} no se encuentra disponible.")

class Camion(Vehiculo):
    def encender(self):
        if self.get_disponibilidad():
            print(f"El motor del camión {self.get_marca} se ha encendido.")
        else:
            print(f"El camión {self.get_marca} no se encuentra disponible.")

carro1 = Carro('Toyota','Corola',2000)
carro2 = Carro('Mazda','CX3',3000)
carro3 = Carro('Mazda','CX5',5000)

"""with open('vehiculos.csv', mode='a', newline='') as file:
    csv_writer = csv.DictWriter(file,fieldnames=carro1.__str__().keys())
    csv_writer.writeheader()
    csv_writer.writerow(carro1.__str__())

with open('vehiculos.csv', mode = 'a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=carro2.__str__().keys())
    csv_writer.writerow(carro2.__str__())
"""

with open('vehiculos.csv', mode = 'a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=carro3.__str__().keys())
    csv_writer.writerow(carro3.__str__())
