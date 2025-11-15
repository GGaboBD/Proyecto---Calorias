from alimentos import mostrar_lista_alimentos, agregar_alimento, buscar_alimento

lista_alimentos = [
    {"nombre": "zanahoria", "calorias": 89}, 
    {"nombre": "manzana", "calorias": 78},
    {"nombre": "banana", "calorias": 58}
]
historial = []
total_calorias = 0
limite_diario = 2000

menu_activo = True

while menu_activo:
    print(" ")
    print("\t      -MENU-")
    print("""
    1:  Mostrar lista de alimentos
    2:  Agregar alimento nuevo
    3:  Buscar alimento
    4:  Editar alimento existente
    5:  Filtrar alimentos por calorías
    6:  Registrar alimento consumido
    7:  Registrar porciones consumidas XXXXXXXXXXX
    8:  Ver historial del día
    9:  Eliminar alimento del historial XXXXXXXXXX
    10: Ver estado de calorías
    11: Ver recomendaciones
    12: Ver estadísticas del día XXXXXXXXXXX
    13: Cambiar límite calórico diario
    14: Reiniciar conteo del día XXXXXXXXX
    15: Salir
    """)
    opcion = input("ingrese una opcion: ")

    if opcion == "1":
        mostrar_lista_alimentos(lista_alimentos)
    elif opcion == "2":
        agregar_alimento(lista_alimentos)
    elif opcion == "3":
        buscar_alimento(lista_alimentos)
    
    elif opcion == "15":
        menu_activo = False