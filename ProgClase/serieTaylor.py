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

def seno(x):
    conta=1
    result = 0 
    for i in range (0,10):
        
        if i%2 == 0:
            result = result + (potencia(x,conta)/factorial(conta))
        else:
            result = result - (potencia(x,conta)/factorial(conta))
            
        #print(conta)
        conta = conta +2
    return result

print(seno(10))