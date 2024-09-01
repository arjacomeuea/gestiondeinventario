import pickle

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        if id in self.productos:
            if nueva_cantidad is not None:
                self.productos[id].set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id].set_precio(nuevo_precio)
        else:
            print("Producto no encontrado")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        with open(archivo, 'rb') as f:
            self.productos = pickle.load(f)


def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de Gestión de Inventario")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Guardar Inventario en Archivo")
        print("7. Cargar Inventario desde Archivo")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido exitosamente.")

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            nueva_cantidad = int(input("Nueva cantidad (deja en blanco para no cambiar): ") or -1)
            nuevo_precio = float(input("Nuevo precio (deja en blanco para no cambiar): ") or -1)
            if nueva_cantidad != -1 or nuevo_precio != -1:
                inventario.actualizar_producto(id, nueva_cantidad if nueva_cantidad != -1 else None, nuevo_precio if nuevo_precio != -1 else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            archivo = input("Nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)
            print(f"Inventario guardado en {archivo}.")

        elif opcion == '7':
            archivo = input("Nombre del archivo desde donde cargar el inventario: ")
            inventario.cargar_inventario(archivo)
            print(f"Inventario cargado desde {archivo}.")

        elif opcion == '8':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
