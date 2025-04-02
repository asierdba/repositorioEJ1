class SerVivo:
    def __init__(self, nombre:str):
        self.nombre = nombre
    
    def __str__(self):
        return self.respirar()
        
    def respirar():
        return "El ser vivo respira. "
    

class Animal(SerVivo):
    def __init__(self, nombre, tipo_reproduccion:str):
        super().__init__(nombre)
        self.tipo_reproduccion = tipo_reproduccion

    def __str__(self):
        return super().__str__() + self.moverse
    
    def moverse(metros = 20):
        return "El animal camina:" + metros + ". "


class Ave(Animal):
    def __init__(self, nombre, tipo_reproduccion, tiene_plumas:bool, puede_volar:bool):
        super().__init__(nombre, tipo_reproduccion)
        self.tiene_plumas = tiene_plumas
        self.puede_volar = puede_volar

    def __str__(self):
        return super().__str__() + self.volar()

    def volar(self):
        if self.puede_volar == True:
            return "Puede volar. "
    

class Mamifero(Animal):
    def __init__(self, nombre, tipo_reproduccion, es_viviparo:bool, tiene_pelo:bool):
        super().__init__(nombre, tipo_reproduccion)
        self.es_viviparo = es_viviparo
        self.tiene_pelo = tiene_pelo

    def __str__(self):
        return super().__str__() + self.amamantar()
    
    def amamantar():
        return "Puede amamantar a sus crias. "
    

class Murcielago(Mamifero, Ave):
    def __init__(self, nombre, tipo_reproduccion, es_viviparo, tiene_pelo, tiene_plumas, puede_volar):
        Mamifero.__init__(nombre, tipo_reproduccion, es_viviparo, tiene_pelo)
        Ave.__init__(nombre, tipo_reproduccion, tiene_plumas, puede_volar)

    def __str__(self):
        return Mamifero().__str__() + Ave().__str__()
    
def main():
    murcielago  = Murcielago("Juanillo", "Mamifera", True, True, False, True)
    print(murcielago)

main()