'''
Version Fn-3
Funcion que elimine los elementos repetido
'''
def unicos(arr):
    resultado = []
    bandera = 0
    for x in range (0,len(arr)):
        bandera = 0
        for y in range (0,len(arr)):
            if arr[y] == arr[x]:
                bandera +=1
        if(bandera == 1):
            resultado.append(arr[x])
    return resultado

print(unicos([9, 3, 1, 3, 9, 2])) # [1, 2]
print(unicos([6, 2, 2, 2, 1, 8])) #[6, 1, 8]
print(unicos([1])) #[1]