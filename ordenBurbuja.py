arr = [86,76,23,98,235,98,21,2,3]

bandera = False
while bandera == False:
    bandera = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            aux = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = aux
            bandera = False
print(arr)