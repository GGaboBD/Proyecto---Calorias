

def mostrar_lista_alimentos(lista_alimentos):
    lista_alimentos.extend([{"nombre": "Zanahoria", "calorias": 89}, 
                            {"nombre": "Manzana", "calorias": 78},
                            {"nombre": "Banana", "calorias": 58}
                           ])

    if len(lista_alimentos) == 0:
        print("No hay alimentos registrados")
    else:
        for i, a in enumerate(lista_alimentos, start=1):
            print(f"{i}. {a["nombre"]} - {a["calorias"]} kcal")

def agregar_alimento(lista_alimentos, nombre, calorias):
    nombre = input("Ingresa el nombre del alimento nuevo a registrar: ").strip().lower()

"""
def registrar_alimento_consumido(lista_comidas):
    sub_menu = True
    alimento_consumido = input("Ingresa el alimento que consumiste este dia: ").lower()

    while sub_menu:
        al = False

        for co in lista_comidas:
            if co["alimento"] == alimento_consumido:
                al = True

        if al == False:
            print("El alimento ingresado no existe en nuestro registro")
            respuesta = input("Desea agregar el alimento al registro? (Si/No)").lower()
            
            if respuesta == "no":
                sub_menu = False

            elif respuesta == "si":
                calorias = input("Ingrese las calorias del alimento (Solo numero): ")
                nuevo_alimento = alimento_consumido

                lista_comidas.append({
                    "alimento": nuevo_alimento,
                    "calorias": calorias,
                })

                print("Alimento agregado al registro")
                sub_menu = False

        else:
            print("Alimento existe en el registro")
            sub_menu = False
"""

        
