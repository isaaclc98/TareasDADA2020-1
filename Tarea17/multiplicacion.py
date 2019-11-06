def multi(lista):
    """
    Esta funcion entrega la multiplicacion de los numeros de una lista
    
    """
    res = 1
    for i in range(len(lista)):
        res = res * lista[i]        
    return res

prueba1 = [1,2,3,4]#24
prueba2 = [1,2]#2
print(multi(prueba1))
print(multi(prueba2))
