'''
Version AL-1.py
De un rango de [2,100] indicar si un numero es primo o no
'''

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

primos=[]
noPrimos=[]
for x in range (2,100):
    if isPrime(x):
        primos.append(x)
    else:
        noPrimos.append(x)
print("Primos: ",primos)
print("\nNo Primos:",noPrimos)


