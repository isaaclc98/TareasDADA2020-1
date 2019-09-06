'''
factorialRec.py
Prog para calcular factorial de manera recursiva
'''
def factorial(x):
    return 1 if (x < 1) else x * factorial(x-1)

num=int(input("Numero: "))
if num >0 and num < 30:
    print("el factorial de ",num,"es: ",factorial(num))
else:
    print("numero no valido")
