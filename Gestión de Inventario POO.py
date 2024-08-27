"""
Ejercicio: Gestión de Inventario
Imagina que estás desarrollando un sistema de gestión de inventario para una tienda. 
Necesitas escribir un programa que permita a los usuarios agregar productos al inventario, 
actualizar la cantidad de productos, eliminar productos y mostrar el inventario actual.
"""

class Producto:
    def __init__(self, nombre, precio,cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad =  cantidad
        
    def actualizar_cantidad (self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        print("------------------------------------------------------------")
        print (f"La cantidad del producto {nombre} se ha actualizado a {cantidad}")
        print("----------------------------------------------------------")
        
class inventario:
    def __init__(self):
        self.lista = []
        

    def crear_producto(self, nombre,precio,cantidad):
        producto = Producto (nombre , precio, cantidad)
        self.lista.append(producto)
        
    def mostrar_inventario(self):
        if not self.lista:
            print ("------------------------------")
            print("Inventario vacio")
            print("-------------------------------------------")
            return
        print("BIENVENIDO AL INVENTARIO ")
        print("--------------------------------")
        for producto in self.lista:
            print(f"Poducto: {producto.nombre}, precio: {producto.precio}, cantidad: {producto.cantidad} ")
            print("---------------------------------")
    
    def eliminar_producto(self, eliminar):
        for producto in self.lista:
            if producto.nombre == eliminar:
                self.lista.remove(producto)
                print("--------------------------------------------------")
                print(f" El producto '{eliminar}' se ha eliminado del inventario.")
                print("--------------------------------------------------")

                break  
            else:
                print("-------------------------------")
                print("Este Poducto no existe en el inventario")
                print("-------------------------------")
    
    def cambiar_cantidad (self, nombre, cantidad):
        for producto in self.lista:
            if producto.nombre == nombre:
                producto.actualizar_cantidad(cantidad)
                break
            else:
                print("-------------------------------")
                print("Este Poducto no existe en el inventario")
                print("-------------------------------")
            

mi_inventario = inventario()

def menu ():
    print("1. Agregar producto")
    print("2. Actualizar cantidad de producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = int(input("introduce una opcion : "))
        if opcion > 5:
            print("-------------------------------")
            print("introduce una opcion valida")
            print("-------------------------------")
        elif opcion == 1:
            nombre = input("Introduce el nombre del producto :")
            precio = input("introduce el precio del producto :")
            cantidad = input("introduce la cantidad del producto : ")
            mi_inventario.crear_producto(nombre,precio,cantidad)
            print("-------------------------------")
            print(f"Se ha agregado al inventario el producto: {nombre} con un precio de: {precio}bs y una cantidad total de: {cantidad}")
            print("-------------------------------")
            
        elif opcion == 2:
            nombre= input("introduce el nombre del producto a actualizar : ")
            cantidad = input("introduce la cantidad nueva : ")
            mi_inventario.cambiar_cantidad(nombre,cantidad)
            
        elif opcion == 3:
            eliminar = input("Introduce el Nombre del producto que deseas eliminar: ")
            mi_inventario.eliminar_producto(eliminar)
            
        elif opcion == 4:
            mi_inventario.mostrar_inventario()
        
        else:
                break




        
    
    
     