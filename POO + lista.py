"""
Ejercicio: Sistema de Reservas de Vuelos
Objetivo:
Crear un sistema sencillo de reservas de vuelos que permita a los usuarios agregar vuelos, hacer reservas, y ver las reservas realizadas.
"""

class Vuelo:
    def __init__(self, codigo, origen, destino, cantidad):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.cantidad = cantidad
        self.reservas = []
        
     
    def hacer_reservas(self, codigo_vuelo, nombre_pasajero):
        if self.cantidad > 0:
            self.reservas.append((codigo_vuelo, nombre_pasajero)) # Fijar como una tupla
            self.cantidad -= 1
            print("------------------------------------------------------------")
            print(f"Se ha reservado el vuelo {codigo_vuelo} para el pasajero: {nombre_pasajero}")
            print("----------------------------------------------------------")
        else:
            print("---------------------------")
            print("El vuelo está lleno")
            print("---------------------------")
        
class SistemaReservas:
    def __init__(self):
        self.vuelos = []
        
    def agregar_vuelo(self, codigo, origen, destino,cantidad):
        vuelo_nuevo = Vuelo(codigo,origen,destino, cantidad)
        self.vuelos.append(vuelo_nuevo)
        
    def hacer_reserva(self, codigo_vuelo, nombre_pasajero):
        for vuelo in self.vuelos:
            if vuelo.codigo == codigo_vuelo :
                vuelo.hacer_reservas(codigo_vuelo, nombre_pasajero)
                break
            else:
                print(".....................")
                print("Este codigo de vuelo no existe")
                print("................................")
                break
        
        
    def mostrar_vuelos(self):
        if not self.vuelos:
            print("-------------------------------")
            print("No hay vuelos disponibles")
            print("-------------------------------")        
        
        print("\n-VUELOS DISPONIBLES") 
        for vuelos in self.vuelos:
            print("-------------------------------------------------------------------")
            print(f"Codigo: {vuelos.codigo}, Origen: {vuelos.origen}, Destino: {vuelos.destino}, Cantidad de asientos: {vuelos.cantidad}")
            print("-------------------------------------------------------------------")
    
            
    def mostrar_reserva(self, codigo_vuelo):
        for vuelo in self.vuelos:
            if vuelo.codigo == codigo_vuelo:
                    print(f"Reservas del vuelo {codigo_vuelo} :{vuelo.reservas}")
             
            if not self.vuelos:
                print("............................")
                print("Vuelo no encontrado")
                print("...............................")       
                break    




def menu():
    print("\n--- Sistema de Reservas de Vuelos ---")
    print("1. Agregar vuelo")
    print("2. Hacer reserva")
    print("3. Mostrar vuelos")
    print("4. Mostrar reservas de un vuelo")
    print("5. Salir")

# Crear el sistema de reservas
sistema = SistemaReservas()

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            codigo = input("Introduce el código del vuelo: ")
            origen = input("Introduce la ciudad de origen: ")
            destino = input("Introduce la ciudad de destino: ")
            capacidad = int(input("Introduce la capacidad del vuelo: "))
            sistema.agregar_vuelo(codigo, origen, destino, capacidad)
            print(f"Vuelo {codigo} agregado exitosamente.")
        
        elif opcion == "2":
            codigo_vuelo = input("Introduce el código del vuelo: ")
            nombre_pasajero = input("Introduce el nombre del pasajero: ")
            sistema.hacer_reserva(codigo_vuelo, nombre_pasajero)
        
        elif opcion == "3":
            sistema.mostrar_vuelos()
        
        elif opcion == "4":
            codigo_vuelo = input("Introduce el código del vuelo: ")
            sistema.mostrar_reserva(codigo_vuelo)
        
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")
