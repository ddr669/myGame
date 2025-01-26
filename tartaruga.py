from turtle import *

def fib():
    b = 1
    c = 1
    print(b)
    f = []
    a = lambda x: x + c
    while True:
        print(a(b), c)
        f.append(a(b))
        c = a(c)
          
        print(a(b))
        b = a(b)
        print(f)
        if b==31:
            
            yield f
    
fib()
speed(0)
teleport(-200,100)
goto(-200,-200)
#fd(20)
#right(2)
clear()
a=0
b=0
while b <= 30:
    #teleport(480,400)
    goto(a,b)
    a -= 4
    b += 2

a = 20
b = -10
while b <= 30:
    #teleport(480,400)
    goto(a,b)
    a += 10
    b -= 20


    
