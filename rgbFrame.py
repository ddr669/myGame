def click():
    k.configure(text=next(t))

def texto():
    lista = ["eu disse para não clicar!",
             "porra!",
             "voce é surdo?",
             "digo, cego!",
             "MORREEEEEEEEEEEEEEEEE"]
    for a in lista:
        yield a

        
class PISCA:
    def __init__(self, surface, color1=(40,20,10), color2=(30,20,80), color3=(20,20,20)):
        self._c1 = color1
        self._c2 = color2
        self._c3 = color3
        self._SURF = surface
        self.color_getter = self.get_color()
        self.start()

    def start(self):
        self._SURF.configure(background=next(self.color_getter))
        self._SURF.after(100, self.start)

    def grad(self, start, r):
        def convHEX(r,g,b):
            return f"#{r:02x}{g:02x}{b:02x}"
        
        out = []
        match r:
            case 0:
                for i in range(int(start[0]), 200):
                        out.append(convHEX(i, start[1], start[2]))
                return out
    
            case 1:
                for i in range(int(start[1]), 160):
                    out.append(convHEX(start[0], i, start[2]))
                return out
            case 2:
                for i in range(int(start[2]), 200):
                    out.append(convHEX(start[0], start[1], i))

                return out
            case _:
                print("error")
                return 0
        
    def configure(self):
        print("oshe")

    def get_color(self):
        def convHEX(r,g,b):
            return f"#{r:02x}{g:02x}{b:02x}"
    
        colors = self.grad(self._c1, r=1)
        reverse = colors[::-1]
      
        while True:
            for c in colors+reverse:
                yield c
    
    '''def get_color(self):
        def convHEX(r,g,b):
            return f"#{r:02x}{g:02x}{b:02x}"
        rw = self.grad((230,150,150), r=0)
        gw = self.grad((80,200,80), r=1)
        bk = [convHEX(10,10,10)]
        colors = self.grad(self._c1, r=0)
        b = self.grad(self._c2, r=2)
        g = self.grad(self._c3, r=1)
        reverse1 = colors[::-1]
        reverse2 = g[::-1]
        reverse3 = b[::-1]
        while True:
            for c in colors+reverse1+g+reverse2+b+reverse3:
                yield c
    '''
if __name__ == "__main__":
    # // <head> //
    from tkinter import *
    import tkinter
    from customtkinter import *
    t = texto()
    c1, c2, c3 = [10,100,80], [50,50,50], [50,50,50]
    def criar(_col1,_col2,_col3,p=0):
        print(_col1,"/n",_col2,"/n",_col3)
        grid_1 = Frame(screen, width=400, height=100)
        PISCA(grid_1, color1=_col1,color2=_col2, color3=_col3)
        return grid_1

    def motion(event):
        x, y = event.x, event.y
        if x in range(0, 20) and y in range(0, 20):
            
            files.configure(fg_color="#000000")
        else:
            files.configure(fg_color="#1B4A40")

    # // </head> // 
    screen = Tk()
    screen.geometry("400x400")
    def degrade(col1, col2, col3,colunaV=0):
        grids = []
        for a in range(0,8):
            grids.append(criar(p=colunaV,_col1=col1,_col2=col2,_col3=col3))
            
            
            
            for b in range(0,len(col1)):
                col1[b], col2[b], col3[b] = col1[b] + a, col2[b] + a , col3[b] + a
        del col1,col2,col3
        return grids


    # // < body > //
    toolbar = CTkFrame(screen, width=400, height=20, corner_radius=5, border_width=1
                       ,border_color="#A3C6A2"
                       ,bg_color="green",fg_color="#1B4A40")
    toolbar.pack(ipady=3)
    files = CTkLabel(screen, width=50, height=20, text="files",text_color="#AAAAAA",fg_color="#1B4A40")
    files.place(x=1,y=2)
    print(help(Event))
    print(files.event.focus())
    files.bind("<Motion>", print)
    
    mouse = screen.bind("<Motion>", motion)
    
    #toolbar = Frame(screen, width=400,height=20,borderwidth=1,background="black")
    #toolbar.pack( anchor="n")
    
    AA = degrade(c1,c2,c3,colunaV=400)
    for A in range(len(AA)-1, 0, -1):
        AA[A].pack(anchor="center")

    
    
    screen.mainloop()
    # // </body> //


    
    #a = PISCA(screen)
    '''label = Frame(screen, width=400, height=70)
    label.pack(anchor="center")
    a = PISCA(label, color1=(20,20,20),color2=(20,20,20), color3=(20,20,20))
    label2 = Frame(screen, width=400, height=60)
    label2.pack(anchor="center")
    a2 = PISCA(label2, color1=(25,25,20),color2=(25,25,25),color3=(25,20,25))
    label3 = Frame(screen, width=400, height=60)
    label3.pack(anchor="center")
    a3 = PISCA(label3, color1=(30,30,30),color2=(30,30,30), color3=(30,30,30))
    label4 = Frame(screen, width=400, height=50)
    label4.pack(anchor="center")
    a4 = PISCA(label4, color1=(40,40,40),color2=(40,40,40),color3=(40,40,40))

    #####
    label5 = Frame(screen, width=400, height=50)
    label5.pack(anchor="center")
    a5 = PISCA(label5, color1=(60,60,60),color2=(60,60,60), color3=(60,60,60))
    label6 = Frame(screen, width=400, height=40)
    label6.pack(anchor="center")
    a6 = PISCA(label6, color1=(70,70,70),color2=(70,70,70),color3=(70,70,70))
    label7 = Frame(screen, width=400, height=40)
    label7.pack(anchor="center")
    a7 = PISCA(label7, color1=(80,80,80),color2=(80,80,80), color3=(80,80,80))
    label8 = Frame(screen, width=400, height=40)
    label8.pack(anchor="center")
    a8 = PISCA(label8, color1=(90,90,90),color2=(90,90,90),color3=(90,90,90))
    
    
    screen.mainloop()
'''
