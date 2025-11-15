def mostrar_lista_alimentos(lista_alimentos): #Opcion 1
    if len(lista_alimentos) == 0:
        print("No hay alimentos registrados")
    else:
        for i, a in enumerate(lista_alimentos, start=1):
            print(f"{i}. {a["nombre"].capitalize()} - {a["calorias"]} kcal")

            
def agregar_alimento(lista_alimentos): #Opcion 2
    nombre = input("Ingresa el nombre del alimento nuevo a registrar: ").lower().strip()

    existe = False

    for a in lista_alimentos:
        if a['nombre'] == nombre:
            existe = True
    if existe:
        print("Ese alimento ya existe en nuestro registro")
    else:
        calorias = int(input("Ingresa las calorias de tu alimento (Solo numeros): "))

        if calorias <=0:
            print("La calorias deben ser mayor a 0")
        else:
            lista_alimentos.append({
                            'nombre': nombre,
                            'calorias':calorias
                        })
            print(f"Agregado: {nombre.capitalize()} - {calorias} kcal")


def buscar_alimento(lista_alimentos): #opcion 3
    nombre = input("Ingresa el nombre del alimento que deseas buscar: ").lower()
    coincidencias = 0

    for a in lista_alimentos:
        if nombre in a['nombre']:
            coincidencias +=1
            print(f"Encontrado. {a['nombre'].capitalize()} - {a['calorias']} kcal")
        
    if coincidencias == 0:
        print("No se encontro tu alimento")
    





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

        
