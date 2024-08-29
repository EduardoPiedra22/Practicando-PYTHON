class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class enlazar :
    def __init__(self):
        self.cabeza = None
        
    def add (self, valor):
        nuevo_nodo =  nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            Corredor = self.cabeza
            while Corredor.siguiente is not None :
                Corredor = Corredor.siguiente
            Corredor.siguiente = nuevo_nodo
    
    def remove (self, valor):
        if self.cabeza == None:
            return False
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return True
   
        Corredor = self.cabeza
        while Corredor.siguiente.valor != valor:
            if Corredor.siguiente == None:
                return False
            else:
                Corredor = Corredor.siguiente
        Deletenodo = Corredor.siguiente
        Corredor.siguiente = Deletenodo
    
    def view (self):
        Corredor = self.cabeza
        while Corredor:
            print(Corredor.valor)
            Corredor = Corredor.siguiente
            
            
            
mi_list = enlazar()
mi_list.add('eduardo')
mi_list.add('piedra')

mi_list.view()
mi_list.remove('eduardo')
mi_list.view()
