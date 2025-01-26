
from tkinter_gradient import GradientFrame as GF
import tkinter as tk
root = tk.Tk()
#tG.Example(root).pack(fill="both", expand=True)
colors1 = [117, 139, 213]
colors2 = [139, 217, 211]





'''
global f
global a
a = GF(root, color1=(255,255,255),color2=(255,255,255), axi=1)
f=0
def col(start=colors1):
    cor1 = next(color_getter)
    cor2 = next(color_getter)
    print(cor1,cor2)
    a = GF(root, color1=cor1,color2=cor2, axi=1)
    a.pack(fill="both",expand=True)
    root.update()
   # colors  = []
    #for i in range(int(start[0]), 255, 10):
       # colors.append([i,start[1],start[2]])
        
   # return colors
   
#
def get_color():
    
    colors  = []
    for i in range(colors1[f], 255, 10):
        colors.append([i,colors1[1],colors1[2]])
        

    reverse = colors[::-1]
    
    for c in colors+reverse:
        yield c
        
        

def change():
    #root.configure(background=next(color_getter))
    a.destroy()
    
    for i in range(0, len(colors2)):
        colors2[i] = colors1[i]
        if int(colors1[i]) >= 200:
            colors1[i] -= 50
        elif int(colors1[i]) <= 20:
            colors1[i] += 50
        else:
            colors1[i] += 10
    
    
    root.after(10, col)    


color_getter = get_color()
while True:
    
    change()
    
    root.mainloop()


'''
