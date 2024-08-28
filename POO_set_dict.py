class Usuario: 
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.roles = set()
    
    def asignar_roles (self, rol):
        self.roles.add(rol)
        
        print("-------------------------------------")
        print(f"se ha agregado el Rol {rol.nombre_rol} a tu usuario {self.nombre}")
        print("-------------------------------------")
        
    
class Rol:
    def __init__(self, nombre_rol, permiso) -> None:
        self.nombre_rol = nombre_rol
        self.permiso = set(permiso)
        
class Sistema:
    def __init__(self) -> None:
        self.usuario = {}
        self.roles = {}
        
    def agregar_usuario(self, nombre, email):
        nuevo_usuario = Usuario(nombre, email)
        self.usuario[email] = nuevo_usuario
        print("-------------------------------------")
        print(f"Usuario {nombre} fue agregado exitosamente")
        print("-------------------------------------")
    
    def agregar_rol(self, nombre_rol, permiso):
        nuevo_rol = Rol(nombre_rol, permiso)
        self.roles[nombre_rol] = nuevo_rol
        print("------------------------------------------")
        print(f"El Rol {nombre_rol} se ha agregado exitosamente")
        print("-------------------------------------------")
        
    def asignar_rol(self, email, nombre_rol):
        if email in self.usuario and nombre_rol in self.roles:
            user = self.usuario[email]
            rol = self.roles[nombre_rol]
            user.asignar_roles(rol)
            
    def mostrar_permisos_usuario (self, email):
        if email in self.usuario:
            usuario = self.usuario[email]
            for rol in usuario.roles: 
                print("--------------------------------")
                print(f"Nombre del rol: {rol.nombre_rol}")
                for permiso in rol.permiso:
                    print("............................")
                    print(f"Permisos : {permiso} ")
        else:
            print(f"No se ha encontrado al un usuario con el corre {email}")
                    
def menu ():
    print("--- Sistema de Gestión de Usuarios ---")
    print("1. Agregar nuevo usuario")
    print("2. Agregar nuevo rol")
    print("3. Asignar rol a usuario")
    print("4. Mostrar permisos de un usuario")
    print("5. Guardar datos en archivo")
    print("6. Cargar datos desde archivo")
    print("7. Salir")

mi_sistema = Sistema()
if __name__ == "__main__":
    while True:
        menu()
        opcion = int(input("Introduce una opcion : "))
        
        if opcion == 1:
            nombre = input("Nombre: ")
            email = input("Email: ")
            mi_sistema.agregar_usuario(nombre, email)
        
        elif opcion == 2:
            nombre_rol = input("Nombre del ROL: ")
            permisos = input("Permisos (separador por coma): ").split(",")
            permiso = {p.strip() for p in permisos}
            mi_sistema.agregar_rol(nombre_rol, permiso)
        
        elif opcion == 3:
            email = input("Correo del Usuario: ")
            nombre_rol = input("Nombre del ROL a asignar : ")
            mi_sistema.asignar_rol(email, nombre_rol)
            
        elif opcion == 4:
            email = input("Email: ")
            mi_sistema.mostrar_permisos_usuario(email)
        