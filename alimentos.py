def registrar_alimento_consumido(lista_comidas):
    sub_menu = True
    while sub_menu:
        alimento_consumido = input("Ingresa el alimento que consumiste este dia: ").lower()
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
            
        })


        
