'''
Version Fn-4
Funcion que saque el promedio de arreglos de la lista
'''

def promed(arr):
    suma = 0
    for x in range(0,len(arr)):
        suma += arr[x]
    promedio = suma / len(arr)
    return promedio

def promLista(arreglo):
    suma = 0
    for i in range (0,len(arreglo)):
        suma += promed(arreglo[i])
    return suma

prueba1 = [[1,2,2,2,2,1],[2,1]] #3.1
prueba2 = [[10,5],[6,2,2],[1]]#11.8
print(promLista(prueba1))    
print(promLista(prueba2))    