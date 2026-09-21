def mostrar_menu():
        print("\nMostrar el Menu")
        print("1 - Ver todos los posts")
        print("2 - Buscar por titulo")
        print("3 - Filtrar por tag")
        print("4 - Crear nuevo post")
        print("5 - Validar posts")
        print("6 - Guardar posts en json")
        print("7 - Salir")


        try:
            opcion = int(input("Seleccioná una opción (1-7): ").strip())
            return opcion
        except ValueError:
                return -1



