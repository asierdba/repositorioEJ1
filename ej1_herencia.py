class Animal:
    def __init__(self, nombre:str, edad:int,  peso:float):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def andar(self, pasos):
        print(f"El animal {self.nombre} ha andado {pasos} pasos.")
        
class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza:str):
        super().__init__(nombre, edad, peso)
        self.raza = raza

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color:str):
        super().__init__(nombre, edad, peso)
        self.color = color

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, especie:str):
        super().__init__(nombre, edad, peso)
        self.especie = especie


def main():
    tipo_animal = input("Tipo de animal (Perro - Gato - Pájaro): ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso: "))

    match tipo_animal:
        case "perro":
            raza = input("Raza: ")
            mi_animal = Perro(nombre, edad, peso, raza)
        case "gato":
            color = input("Color: ")
            mi_animal = Gato(nombre, edad, peso, color)
        case "pajaro":
            especie = input("Especie: ")
            mi_animal = Pajaro(nombre, edad, peso, especie)

    pasos = input("¿Cuántos pasos ha dado el animal?: ")
    mi_animal.andar(pasos)
    
main()