'''
Version A-4
Determinar el promedio de alumnos que aprobaron el curso
'''
def promed(arr):
    suma = 0
    for x in range(0,len(arr)):
        suma += arr[x]
    promedio = suma / len(arr)
    return promedio
def approved(alumnos):
    aprobados = 0
    for i in range (0,len(alumnos)):
        if promed(alumnos[i]) >= 6:
            aprobados += 1
    resultado = aprobados / len(alumnos)
    return resultado * 100


prueba10 = [[9,8,7,5,2],[5,5,5,5,5,5],[0,1,2],[4,2,4,5,7,8],[1,1,1,1]] #20
print(approved(prueba10),"%")