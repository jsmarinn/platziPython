# Concesionario donde se venden y se compran vehículos
# Un usuario puede vender o comprar vehículos

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponibilidad = True
    
    def get_disponibilidad(self):
        return self.disponibilidad

    def set_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def get_precio(self):
        return self.precio

class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.vehiculos_propios = []

    def listarVehiculosPropios(self):
        for vehiculo in self.vehiculos_propios:
            print(f"{vehiculo.marca} con modelo {vehiculo.modelo}")

class Concesionario:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []

    def comprar_vehiculo(self, vehiculo, cliente):
        if vehiculo in self.vehiculos:
            print(f"El vehículo con marca {vehiculo.marca} y modelo {vehiculo.modelo} ya se encuentra en el concesionario")
        else:
            self.vehiculos.append(vehiculo)
            cliente.vehiculos_propios.remove(vehiculo)
            vehiculo.set_disponibilidad(True)

    def vender_vehiculo(self, vehiculo, cliente):
        if vehiculo in self.vehiculos:
            cliente.vehiculos_propios.append(vehiculo)
            vehiculo.set_disponibilidad(False)
            self.vehiculos.remove(vehiculo)
            print(f"El vehículo con marca {vehiculo.marca} y modelo {vehiculo.modelo} se ha vendido con éxito")
        else:
            print(f"El vehículo con marca {vehiculo.marca} y modelo {vehiculo.modelo} no se encuentra disponible para la venta.")

    def listar_vehiculos_disponibles(self):
        for vehiculo in self.vehiculos:
            if vehiculo.disponibilidad:
                print(f"{vehiculo.marca} - {vehiculo.modelo} - {vehiculo.precio}")

concesionario = Concesionario()

v1 = Vehiculo("Toyota","2023","2600")
v2 = Vehiculo("Mercedes","2024","30000")
v3 = Vehiculo("Renault","2025","1500")

u1 = Usuario("Juan","001")

concesionario.vehiculos.append(v1)
concesionario.vehiculos.append(v2)
concesionario.vehiculos.append(v3)

concesionario.clientes.append(u1)

concesionario.listar_vehiculos_disponibles()

concesionario.vender_vehiculo(v1,u1)

concesionario.listar_vehiculos_disponibles()

concesionario.vender_vehiculo(v1,u1)

concesionario.comprar_vehiculo(v1,u1)

concesionario.listar_vehiculos_disponibles()




        




