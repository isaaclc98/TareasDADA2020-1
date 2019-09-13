'''
serieTaylor.py
'''
def factorial(x):
    return 1 if (x < 1) else x * factorial(x-1)
def potencia(base,exp):
    if(exp == 0):
        return 1
    else:
        return base * potencia(base,exp-1)

def seno(rad):
    x = rad * 3.141592 / 180
    result = 0 
    for i in range (51):
        n = (2+i)-1
        if i%2 == 0:
            result = result - (potencia(x,n)/factorial(n))
        else:
            result = result + (potencia(x,n)/factorial(n))
    return result

print(seno(3.1416/2))