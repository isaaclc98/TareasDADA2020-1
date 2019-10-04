'''
Version A-2
examen.py
'''
def divisiblePor(lista,divisor):
    resultado = []
    for x in range (0,len(lista)):
        
        if lista[x]!= 0 and lista[x]%divisor == 0:
            resultado.append(lista[x])
    return resultado

lista1=[1,2,3,4,5,6]#2,4,6
lista2=[9,12,3,0,1,4]#9,12,3
lista3=[10,11,3]#10,11,3
print(divisiblePor(lista1,2))
print(divisiblePor(lista2,3))
print(divisiblePor(lista3,1))