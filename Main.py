from alimentos import mostrar_lista_alimentos

lista_alimentos = []
historial = []
total_calorias = 0
limite_diario = 2000

print(" ")
print("\t      -MENU-")
print("""
1:  Mostrar lista de alimentos
2:  Agregar alimento nuevo
3:  Editar alimento existente
4:  Buscar alimento
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