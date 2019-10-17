'''
linearSearch.py
busca un elemento en un arreglo de 10.000 numeros enteros aleatorios
'''
import random

def busca(lista,x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

lista = [random.randint(0,100) for _ in range(10000)]
print(busca(lista,7))
print(busca(lista,99))
print(busca(lista,101))
print(busca(lista,44))
