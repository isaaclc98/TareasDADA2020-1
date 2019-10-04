'''
Version L-1
Utilizando ciclos for dibujar piramide de numeros nones
'''
resultado = ""
fila = 1
for i in range (1,11):
    print(i," -  ",end="")
    for x in range(0,i):
        print(x*2+1,end="")
    print(" ")
