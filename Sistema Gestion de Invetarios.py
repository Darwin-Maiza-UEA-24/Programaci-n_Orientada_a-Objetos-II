class Producto:
    def __init__(self, id, nombre, tipo, plataforma, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.plataforma = plataforma
        self.cantidad = cantidad
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificar si el ID ya existe
        if any(p.id == producto.id for p in self.productos):
            print("El producto con ese ID ya existe")
            return
        self.productos.append(producto)

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print(f"Producto con ID {id} eliminado.")
                return
        print(f"Producto con ID {id} no encontrado.")

    def actualizar_producto(self, id, nuevo_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id == id:
                if nuevo_cantidad:
                    producto.cantidad = nuevo_cantidad
                if nuevo_precio:
                    producto.precio = nuevo_precio
                print(f"Producto con ID {id} actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Búsqueda insensible a mayúsculas y minúsculas
        resultados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(
                    f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Plataforma: {producto.plataforma}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
        else:
            print("El inventario está vacío.")


# Función para el menú interactivo
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            # Añadir producto
            id_producto = int(input("Introduce el ID del producto: "))
            nombre = input("Introduce el nombre del producto: ")
            tipo = input("Introduce el tipo del producto (Juego, Consola, Accesorio): ")
            plataforma = input("Introduce la plataforma del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))

            producto = Producto(id_producto, nombre, tipo, plataforma, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Eliminar producto
            id_producto = int(input("Introduce el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar producto
            id_producto = int(input("Introduce el ID del producto a actualizar: "))
            cantidad = input("Introduce la nueva cantidad del producto (deja en blanco para no modificar): ")
            precio = input("Introduce el nuevo precio del producto (deja en blanco para no modificar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            # Buscar producto
            nombre = input("Introduce el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            print("Productos encontrados:")
            for producto in resultados:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Plataforma: {producto.plataforma}")

        elif opcion == "5":
            # Mostrar inventario
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Salir
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecución del menú
menu()
