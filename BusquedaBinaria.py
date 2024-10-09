def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) -1
    

    while izquierda <= derecha:
        medio = izquierda + (derecha-izquierda)//2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
            
        elif lista[medio] > objetivo:
            derecha = medio - 1
        
    return -1
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
resultado = busqueda_binaria(lista, 6)

if resultado != -1:
    print(f"El numero encontrado esta en el indice: {resultado}")
else:
    print("numero no encontrado")
