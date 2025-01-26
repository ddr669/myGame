from tkinter import *
from random import randint
from tkinter_gradient import GradientFrame as GF

screen = Tk()
screen.geometry("600x600")
global col1
global col2
global b

col2 = [0,0,0]
col1 = [0,0,0]
col = []
b = GF(screen, color1=col1, color2=col2,axi=0)
for a in range(0,255):
    col.append(a)
    
def grad(start,r = randint(0,2)):
    
    def convHEX(r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"

    out = []
    match r:
        case 0:
            for i in range(int(start[0]), 255):
                out.append(convHEX(start[0], start[1], i))
            return out
    
        case 1:
            for i in range(int(start[0]), 255):
                out.append(convHEX(start[0], i, start[2]))
            return out
        case 2:
            for i in range(int(start[0]), 226):
                out.append(convHEX(i, start[1], start[2]))

            return out
        case _:
            print("error")
            return 0
def get_color():
    colors = grad([150,110,150], r=2)
    reverse = colors[::-1]
    
    
    while True:
        for c in colors+reverse:
            yield c

            
def start():
    screen.configure(background=next(color_getter))
    
    screen.after(20, start)

def change(cor1=(255,100,10),cor2=(255,255,255)):
    
    b = GF(screen, color1=(255,100,100), color2=(255,255,255),axi=1)
    b.pack()
if __name__ == "__main__":  
    color_getter = get_color()
    start()

    screen.mainloop()
