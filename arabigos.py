num=int(input("Introduce un numero desde el 1, hasta el 3900: "))
while(num!=0 and num<3901):
    if(num <= 3900 and num>=1000):
        print("M",end="")
        num=num-1000
    elif(num<1000 and num>=900):
        print("CM",end="")
        num=num-900
    elif(num<900 and num>500):
        print("D",end="")
        num=num-500
    elif(num==500):
        print("D",end="")
        num=num-500
    elif(num<500 and num>400):
        print("CD",end="")
        num=num-400
    elif(num<400 and num>99):
        print("C",end="")
        num=num-100
    elif(num<100 and num>89):
        print("XC",end="")
        num=num-90
    elif(num<90 and num>59):
        print("L",end="")
        num=num-50
    elif(num<60 and num>=50):
        print("L",end="")
        num=num-50
    elif(num<50 and num>39):
        print("XL",end="")
        num=num-40
    elif(num<40 and num>=10):
        print("X",end="")
        num=num-10
    elif(num==9):
        print("lX",end="")
        num=num-9
    elif(num<=8 and num>=6):
        print("V",end="")
        num=num-5
    elif(num==5):
        print("V",end="")
        num=num-5
    elif(num==4):
        print("lv",end="")
        num=num-4
    elif(num<=3 and num>=1):
        print("l",end="")
        num=num-1
    
print ("")
        

    



