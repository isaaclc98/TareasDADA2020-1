def busquedaBinaria(lista,mini,maxi,x):
    if mini > maxi:
        return -1
    if maxi >= mini:
        medio = (maxi+mini)//2
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            return busquedaBinaria(lista,mini,medio-1,x)
        else:
            return busquedaBinaria(lista,medio+1,maxi,x)
    else:
        return -1
prueba1= [1,2,3,5,6,9,11]
print(busquedaBinaria(prueba1,0,len(prueba1)-1,50))#-1
print(busquedaBinaria(prueba1,0,len(prueba1)-1,1))#0
print(busquedaBinaria(prueba1,0,len(prueba1)-1,4))#-1
print(busquedaBinaria(prueba1,0,len(prueba1)-1,11))#6