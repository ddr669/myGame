import numpy as np
import turtle as t
from random import randint

t.color("black")
t.fillcolor("blue")
t.delay(0.00)
colors = ["blue","green","red"]#,"pink","yellow","gray","purple"]
def fib(value):
    n1, n2 = 0, 1
    count = 0
    f = []
    while count < value:
        print(n1)
        nth = n1 + n2
        f.append(nth)
       # update values
        n1 = n2
        n2 = nth
        count +=1
    return f

f = fib(9)
f.reverse()
print(f)

def mais(fV):
    for a in range(0, len(fV)):
        fV[a] = fV[a] + 1
    return fV
def espiral():
    v = 0
    for a in f:
        t.right((np.pi*a))
        t.fd(1)
        v += 1
    while v != 100:
        for a in f:
            t.right((np.pi*(a/v))*2)
            t.fd(1)
        v += 1
espiral()
t.mainloop()


