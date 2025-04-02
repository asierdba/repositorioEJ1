from abc import abstractmethod


class Productos:
    def __init__(self, nombre, fecha_caducidad, numero_lote, peso, medida):
        self.nombre = nombre
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
        self.peso = peso
        self.medida = medida

    def __str__(self):
        return f"Nombre: {self.nombre} ||| Fecha caducidad: {self.fecha_caducidad} ||| Número de lote: {self.numero_lote} ||| Peso: {self.peso} ||| Medida: {self.medida} ||| "

    @abstractmethod
    def calcular_coste_envio(self):
        return self.peso * 3


class Fresco(Productos):
    def __init__(self,nombre, fecha_caducidad, numero_lote, peso, medida, fecha_envasado, pais_origen):
        super().__init__(nombre, fecha_caducidad, numero_lote, peso, medida)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def __str__(self):
        return f"{super().__str__()} ||| Fecha envasado: {self.fecha_envasado} ||| País origen: {self.pais_origen}. "

    def calcular_coste_envio(self):
        return int(super().calcular_coste_envio())

class Refrigerado(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, peso, medida, cod_organismo):
        super().__init__(nombre, fecha_caducidad, numero_lote, peso, medida)
        self.cod_organismo = cod_organismo

    def __str__(self):
        return f"{super().__str__()} ||| Código organismo: {self.cod_organismo}."

    def calcular_coste_envio(self):
        return int(super().calcular_coste_envio()) + 2

class Congelado(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, peso, medida, temperatura_recomendada):
        super().__init__(nombre, fecha_caducidad, numero_lote, peso, medida,)
        self.temperatura_recomendada = temperatura_recomendada

    def __str__(self):
        return f"{super().__str__()} ||| Temperatura recomendada: {self.temperatura_recomendada}."

    def calcular_coste_envio(self):
        return int(super().calcular_coste_envio()) + 5



def main():
    pregunta = ""
    while pregunta.upper() != "N":
        opcion = "S"
        lista_tipos = ["Fresco", "Refrigerado", "Congelado"]
        lista_frescos = []
        lista_refrigerados = []
        lista_congelados = []
        lista_todos = []

        while opcion.upper() == "S":

            print("TIPO DE PRODUCTOS:")
            for indice, elemento in enumerate(lista_tipos):
                print(f"{indice + 1}. {elemento}")

            producto = int(input("¿Qué tipo de producto vas a añadir? Escribe su número: "))

            if producto == 1 or producto == 2 or producto == 3: 
                nombre = input("Nombre: ")
                fecha_cad = input("Fecha de caducidad: ")
                num_lote = input("Numero lote: ")
                peso = int(input("Peso: "))
                medida = int(input("Medida: "))
                
                match producto:
                    case 1:
                        fecha_enva = input("Fecha de envasado: ")
                        pais_ori = input("País de origen: ")
                        mi_producto = Fresco(nombre, fecha_cad, num_lote, peso, medida, fecha_enva, pais_ori)
                        lista_frescos.append(mi_producto)

                    case 2:
                        cod_org = input("Código organización: ")
                        mi_producto = Refrigerado(nombre, fecha_cad, num_lote, peso, medida, cod_org)
                        lista_refrigerados.append(mi_producto)

                    case 3:
                        tem_reco = input("Temperatura recomendada: ")
                        mi_producto = Congelado(nombre, fecha_cad, num_lote, tem_reco, peso, medida)
                        lista_congelados.append(mi_producto)
                
                lista_todos.append(mi_producto)
                opcion = input("¿Quieres seguir añadiendo productos? Para seguir escribe: 'S': ")

        ver = input("¿Quieres ver la lista de productos actual? S/N: ")

        while True:

            if ver.upper() == "S":

                tipo = input("¿Que lista quieres ver (Frescos, Refrigerados, Congelados o todos?: ").lower()

                match tipo:
                    case "frescos":
                        for indice, elemento in enumerate (lista_frescos):
                            print(f"{indice + 1}. {elemento}")
                        print("")

                        seleccion = input("Dime el número del elemento del que quieres saber su coste de envío o pulsa 'N'.")
                        if seleccion == "N":
                            pass
                        else:
                            print(f"Precio envio: {lista_frescos[int(seleccion) - 1].calcular_coste_envio()} €")
                        
                        borrar = input("¿Quieres borrar algún elemento? (S/N): ")
                        if borrar.upper() == "S":
                            elemento_borrar = input("¿Qué número?: ")
                            lista_frescos[elemento_borrar - 1].pop
                        break

                    case "refrigerados":
                        for indice, elemento in enumerate (lista_refrigerados):
                            print(f"{indice + 1}. {elemento}")
                        print("")
                        
                        seleccion = input("Dime el número del elemento del que quieres saber su coste de envío o pulsa 'N'.")
                        if seleccion == "N":
                            pass
                        else:
                            print(f"Precio envio: {lista_refrigerados[int(seleccion) - 1].calcular_coste_envio()} €")
                        
                        borrar = input("¿Quieres borrar algún elemento? (S/N): ")
                        if borrar.upper() == "S":
                            elemento_borrar = input("¿Qué número?: ")
                            lista_refrigerados[elemento_borrar - 1].pop
                        break

                    case "congelados":
                        for indice, elemento in enumerate (lista_congelados):
                            print(f"{indice + 1}. {elemento}")
                        print("")
                        
                        seleccion = input("Dime el número del elemento del que quieres saber su coste de envío o pulsa 'N'.")
                        if seleccion == "N":
                            pass
                        else:
                            print(f"Precio envio: {lista_congelados[int(seleccion) - 1].calcular_coste_envio()} €")
                        
                        borrar = input("¿Quieres borrar algún elemento? (S/N): ")
                        if borrar.upper() == "S":
                            elemento_borrar = input("¿Qué número?: ")
                            lista_congelados[elemento_borrar - 1].pop
                        break

                    case "todos":
                        for indice, elemento in enumerate (lista_todos):
                            print(f"{indice + 1}. {elemento}")
                        print("")
                        seleccion = input("Dime el número del elemento del que quieres saber su coste de envío o pulsa 'N'.")
                        
                        if seleccion == "N":
                            pass
                        else:
                            print(f"Precio envio: {lista_todos[int(seleccion) - 1].calcular_coste_envio()} €")
                        
                        borrar = input("¿Quieres borrar algún elemento? (S/N): ")
                        if borrar.upper() == "S":
                            elemento_borrar = int(input("¿Qué número?: "))
                            lista_todos[elemento_borrar - 1].pop
                        break

                    case _: 
                        print("Lista no existente.")

            elif ver.upper() == "N":
                break

            else:
                print("Comando invalido.")

        pregunta = input("¿Quieres seguir usando el programa, 'N' para salir?): ")
main()