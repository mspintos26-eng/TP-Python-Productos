productos = []
opcion = ""
while opcion != "5":
    print("\n===== SISTEMA DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    
    if opcion == "1":
       
        nombre = input("Ingresa el nombre del producto: ").strip()

        while nombre == "":
            print("Error: el nombre no puede estar vacio.")
            nombre = input("Ingresa el nombre del producto: ").strip()

        categoria = input("Ingresa la categoria: ").strip()

        while categoria == "":
            print("Error: la categoria no puede estar vacia.")
            categoria = input("Ingresa la categoria: ").strip()

        
        precio_texto = input("Ingresa el precio: ").strip()

        while not precio_texto.isdigit() or int(precio_texto) <= 0:
            print("Error: ingresa un precio entero mayor que cero.")
            precio_texto = input("Ingresa el precio: ").strip()

        precio = int(precio_texto)


        producto = [nombre, categoria, precio]
        productos.append(producto)

        print("Producto registrado correctamente")


    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\nPRODUCTOS REGISTRADOS")

            for i in range(len(productos)):
                print(f"\nProducto {i + 1}")
                print(f"Nombre: {productos[i][0]}")
                print(f"Categoria: {productos[i][1]}")
                print(f"Precio: ${productos[i][2]}")


   
    elif opcion == "3":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            
            buscar = input("Ingresa el nombre del producto a buscar: ").strip().lower()

            while buscar == "":
                print("Error: debes ingresar un nombre para buscar.")
                buscar = input("Ingresa el nombre del producto a buscar: ").strip().lower()

            encontrado = False
            for producto in productos:
                if producto[0].lower() == buscar:
                    print("Producto encontrado:")
                    print(f"Nombre: {producto[0]}")
                    print(f"Categoria: {producto[1]}")
                    print(f"Precio: ${producto[2]}")
                    encontrado = True

            if encontrado == False:
                print("No se encontraron productos con ese nombre.")


    
    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar.")
        else:
            print("\nPRODUCTOS REGISTRADOS")

            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i][0]} - ${productos[i][2]}")

            
            numero_texto = input("Ingresa el numero del producto a eliminar: ").strip()

            while not numero_texto.isdigit() or int(numero_texto) < 1 or int(numero_texto) > len(productos):
                print("Error: ingresa un numero de producto valido.")
                numero_texto = input("Ingresa el numero del producto a eliminar: ").strip()

            numero = int(numero_texto)


            if numero >= 1 and numero <= len(productos):
                eliminado = productos.pop(numero - 1)
                print(f"Se elimino el producto: {eliminado[0]}")
            else:
                print("Numero de producto incorrecto.")


    elif opcion == "5":
        print("Saliendo del programa...")

    else:
        print("Opcion incorrecta. Intenta nuevamente.")
