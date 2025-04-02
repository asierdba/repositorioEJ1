from abc import abstractmethod
import math

class Figuras:
    def __init__(self, nombre:str):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_area(self, radio):
        pass
    

class Cuadrado(Figuras):
    def __init__(self, nombre):
        super().__init__(nombre)

    def perimetro(lado):
        return lado * 4
    
    def diagonal(perimetro):
        return perimetro / 4 * math.sqrt(2) 


class Circulo(Figuras):
    def __init__(self, nombre):
        super().__init__(nombre)

    def circunferencia(radio):
        return 2 * math.pi * radio

    def diametro(radio):
        return 2 * radio

class Triangulo(Figuras):
    def __init__(self, nombre):
        super().__init__(nombre)

    def perimetro(lado1, lado2, lado3):
        return lado1 + lado2 + lado3

    def altura(base, altura):
        area = base * altura
        return 2 * area / base
    


def main():
    figura = input("¿Qué figura quieres calcular? (Cuadrado, Circulo, Triangulo)")
    nombre_figura = str(input("Nombre de la figura: "))

    match figura:
        case "cuadrado":
            mi_figura = Cuadrado(nombre_figura)
            calculo = input("Calcular: Perimetro/Diagonal: ")
            if calculo == "Perimetro":
                resultado = mi_figura.perimetro(input("¿Cuánto mide el lado?: "))
            elif calculo == "Diagonal":
                resultado = mi_figura.diagonal(mi_figura.perimetro(input("¿Cuánto mide el lado?: ")))
        
        case "ciculo":
            mi_figura = Circulo(nombre_figura)
            calculo = input("Calcular: Circunferencia/Diametro: ")
            if calculo == "Circunferencia":
                resultado = mi_figura.circunferencia(input("¿Cuánto mide el radio?: "))
            elif calculo == "Diametro":
                resultado = mi_figura.diametro(input("¿Cuánto mide el radio?: "))
        
        case "triangulo":
            mi_figura = Triangulo(nombre_figura)
            calculo = input("Calcular: Circunferencia/Diametro: ")
            if calculo == "Perimetro":
                resultado = mi_figura.perimetro(input("Lado 1: "), input("Lado 2: "), input("Lado 3: "))
            elif calculo == "Altura":
                resultado = mi_figura.altura(input("Base del triangulo: "), input("Altura: "))

    print(f"El resultado de la operación es: {resultado}")

main()