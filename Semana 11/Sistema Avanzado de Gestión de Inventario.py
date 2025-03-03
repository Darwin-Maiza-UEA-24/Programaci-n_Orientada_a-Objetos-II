import os

class Producto:
    def __init__(self, id, nombre, tipo, plataforma, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.plataforma = plataforma
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Plataforma: {self.plataforma}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    @classmethod
    def from_string(cls, linea):
        """Convierte una línea de texto en un objeto Producto."""
        datos = linea.strip().split(",")
        return cls(int(datos[0]), datos[1], datos[2], datos[3], int(datos[4]), float(datos[5]))

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = []
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as file:
                    for linea in file:
                        productos.append(Producto.from_string(linea))
                print("Inventario cargado desde archivo.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.tipo},{producto.plataforma},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado en archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("El producto con ese ID ya existe.")
            return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto agregado al inventario.")

    def eliminar_producto(self, id):
        producto_encontrado = False
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                producto_encontrado = True
                break
        if producto_encontrado:
            self.guardar_inventario()
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Producto con ID {id} no encontrado.")

    def actualizar_producto(self, id, nuevo_cantidad=None, nuevo_precio=None):
        producto_encontrado = False
        for producto in self.productos:
            if producto.id == id:
                if nuevo_cantidad is not None:
                    producto.cantidad = nuevo_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                producto_encontrado = True
                break
        if producto_encontrado:
            self.guardar_inventario()
            print(f"Producto con ID {id} actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

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
            id_producto = int(input("Introduce el ID del producto: "))
            nombre = input("Introduce el nombre del producto: ")
            tipo = input("Introduce el tipo del producto (Juego, Consola, Accesorio): ")
            plataforma = input("Introduce la plataforma del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))

            producto = Producto(id_producto, nombre, tipo, plataforma, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = int(input("Introduce el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = int(input("Introduce el ID del producto a actualizar: "))
            cantidad = input("Introduce la nueva cantidad del producto (deja en blanco para no modificar): ")
            precio = input("Introduce el nuevo precio del producto (deja en blanco para no modificar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("Productos encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
