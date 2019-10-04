'''
Version A-1
Encontrar el numero faltante de 0 a 9
'''
def faltante(arr):
    total=45
    aux=0
    for i in range (0,len(arr)):
        aux += arr[i]
    if total == aux and len(arr) >=10:
        print("No falta ningun numero")
    else:
        print("Falta el numero", total-aux)

prueba1 = [2, 1, 9, 3, 8, 7, 4, 6, 0] #5
prueba2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]#0
prueba3 = [2, 1, 9, 3, 8, 7, 4, 6, 0,5]#ninguno

faltante(prueba1)
faltante(prueba2)
faltante(prueba3)
