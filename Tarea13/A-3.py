'''
Version A-3.py
Dado un arrgeglo, contar numeros positivos y suma negativos
El 0 no cuenta
'''

def cuentaPosSumNeg(arr):
    positivos = 0
    negativos = 0
    for i in range(0,len(arr)):
        if arr[i] < 0:
            negativos += arr[i]
        else:
            positivos +=1
    print(positivos," positivos, ",negativos," es la suma de los negativos")

prueba1 = [1,2,3,4,5,6,-11,-12,-13,-14,-15]#6 y -65

cuentaPosSumNeg(prueba1)