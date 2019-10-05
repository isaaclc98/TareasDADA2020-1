'''
Version Fn-6.py
Crear una funsion que sume la diferencia de los consecutivos en una lista
'''

def sumDif(arr):
    for i in range (0,len(arr)):
        diferencia = arr[0]
        diferencia = diferencia - arr[i]
    print (diferencia)

prueba1 = [10,2,1]#9
prueba2 = [11,10,5]#6
prueba3 = [4,3,2,1]#3
prueba4 = [1,2,3,4]#-3

sumDif(prueba1)
sumDif(prueba2)
sumDif(prueba3)
sumDif(prueba4)