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

