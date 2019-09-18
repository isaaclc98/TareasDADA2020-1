'''
forArabigo.py
'''
def arabToRomano(num):
    resultado = ""
    while(num!=0 and num<3901):
        if(num <= 3900 and num>=1000):
            resultado = resultado +"M"
            num=num-1000
        elif(num<1000 and num>=900):
            resultado = resultado +"CM"
            num=num-900
        elif(num<900 and num>500):
            resultado = resultado +"D"
            num=num-500
        elif(num==500):
            resultado = resultado +"D"
            num=num-500
        elif(num<500 and num>=400):
            resultado = resultado +"CD"
            num=num-400
        elif(num<400 and num>99):
            resultado = resultado +"C"
            num=num-100
        elif(num<100 and num>89):
            resultado = resultado +"XC"
            num=num-90
        elif(num<90 and num>59):
            resultado = resultado +"L"
            num=num-50
        elif(num<60 and num>=50):
            resultado = resultado +"L"
            num=num-50
        elif(num<50 and num>39):
            resultado = resultado +"XL"
            num=num-40
        elif(num<40 and num>=10):
            resultado = resultado +"X"
            num=num-10
        elif(num==9):
            resultado = resultado +"lX"
            num=num-9
        elif(num<=8 and num>=6):
            resultado = resultado +"V"
            num=num-5
        elif(num==5):
            resultado = resultado +"V"
            num=num-5
        elif(num==4):
            resultado = resultado +"lv"
            num=num-4
        elif(num<=3 and num>=1):
            resultado = resultado +"l"
            num=num-1
    return resultado

#print(arabToRomano(400))
for x in range(3901):
    print(x," ",arabToRomano(x))