# He realizado un cambio.

# PRUEBA DE MODIFICACIÓN
prueba = 0

class Vehiculo:
    def __init__(self):
        self.kilometros_recorridos = 0
        self.kilometros_totales = 0
        self.color = ""
        self.marca = ""

    def circular(self):
        self.kilometros_recorridos = int(input("Kilometros recorridos: "))
        self.kilometros_totales += self.kilometros_recorridos
        return self.kilometros_totales

class Bicicleta(Vehiculo):
    def __init__(self):
        super(Vehiculo).__init__()
        self.ruedas = 2

    def crear_bicicleta(self):
        self.marca = input("Introduce la marca")
        self.color = input("Introduce el color: ")
        self.kilometros_totales = int(input("Introduce los kilometros totales: "))

    def cambio_ruedas(self):
        if self.kilometros_totales > 1000:
            print("Se recomienda el cambio de ruedas.")

class Coche(Vehiculo):
    def __init__(self):
        super(Vehiculo).__init__()
        self.ruedas = 4
        self.motor = ""

    def crear_coche(self):
        self.marca = input("Introduce la marca")
        self.color = input("Introduce el color: ")
        self.motor = input("Introduce el motor: ")
        self.kilometros_totales = int(input("Introduce los kilometros totales: "))

    def cambio_ruedas(self):
        if self.kilometros_totales > 10000:
            print("Se recomienda el cambio de ruedas.")
