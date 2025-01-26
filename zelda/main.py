import pygame as pg
import numpy as np
from  _config_ import _WIDTH, _HEIGHT, _CENTER, _PLAYER
from _config_ import _R, _G, _B
from _config_ import convertHEX
from _config_ import gradient
import numpy as np
from random import randint
class attr:
    def raycasting(self, x,y,z) -> int:
        pg.draw.line(self._screen, convertHEX(20,10,180), pg.Vector2(_WIDTH/2, _HEIGHT), pg.Vector2(x, y))
        return 1
    def camera(self, x, y, z) -> np.array:
        if y < 80:
            pg.mouse.set_pos([_WIDTH/2,_HEIGHT/2])
            return np.array([x,y+np.pi/2,z])
class Random_Short:
    def __init__(self, lista):
        self.lista = lista
        while self.lista:
            lista = self._random()
            print(self._verify(lista))
        
            
    def _random(self)->list:
        tmp = self.lista
        index_ran = randint(0, len(self.lista))
        if index_ran == 0 and self.lista[0] > self.lista[index_ran+1]:
            tmp[0] = self.lista[1]
            tmp[1] = self.lista[0]
            return tmp
        if index_ran == len(self.lista) and self.lista[index_ran] < self.lista[index_ran-1]:
            tmp[index_ran] = self.lista[index_ran-1]
            tmp[index_ran-1] = self.lista[index_ran]
            return tmp
        if self.lista[index_ran] > self.lista[index_ran-1]:
            tmp[index_ran] = self.lista[index_ran-1]
            tmp[index_ran-1] = self.lista[index_ran]
            return tmp
        print("!")
    def _verify(self, lista):
        var = lista[::-1]
        index = 0
        while index!=len(var):
            if var[index] != 0 and var[index] < var[index-1]:
                break
                
            index += 1
        else:
            print("WWW")
            return 0
        print(lista)
        self.lista = None
        return 1
    
            
            
        
        
        
class Game(attr):
    super(attr)
    def __init__(self):
        pg.init()
        self.running = True
        #self.floor = np.array()
        self.r,self.g,self.b = _R,_G,_B
        self.piscola = self.get_color()
        self.r = 110
        self.g = 100
        self.b = 90
        self.clock = pg.time.Clock()
        self._screen=pg.display.set_mode((_WIDTH, _HEIGHT))
        self.screen=pg.Surface((_WIDTH, _HEIGHT), pg.SRCALPHA, 32).convert_alpha()
        self.posicao = np.array([1, 1, 1])
    def anima(self):
        pass
    
    def get_color(self):
        colors_b = gradient(r=False,b=True)
        color_p = gradient(p=True, r=False)
        
        colors_r = gradient(r=True,b=False,g=False)
        color_y = gradient(r=False,y=True)
        
        colors_g = gradient(g=True,b=False,r=False)
        
    
        reverse_b = colors_b[::-1]
        reverse_r = colors_r[::-1]
        reverse_g = colors_g[::-1]
        while True:
            for c in colors_r+reverse_r+color_y+color_y[::-1]+colors_g+reverse_g+colors_b+reverse_b+color_p+color_p[::-1]:
                yield c

    def render(self, matrix) -> list :
   
       # self._screen.blit(self.screen, dest=(0,0))
   
        for a in range(0, len(matrix)):
            pg.draw.line(self._screen, convertHEX(120,210,90),matrix[a][0], matrix[a][1])
            
    def run(self):
        x, y ,z= _WIDTH/2, _HEIGHT/2, 1
        self.perso = [[pg.Vector2(0,y),pg.Vector2(_WIDTH,y)],[pg.Vector2(x,0),pg.Vector2(x,_HEIGHT)]]
        
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self._screen.fill(next(self.piscola))
            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                pg.quit()
                self.running = False
            if keys[pg.K_w]:
                pass
            if pg.mouse.get_focused():
                pass
            #render -> linha -> ponto
            self.raycasting(x,y,1)
            # linha do mouse debug
            self.render(self.perso)
            y = pg.mouse.get_pos()[1]
            x = pg.mouse.get_pos()[0]
            
            self.perso = [[pg.Vector2(0,y),pg.Vector2(_WIDTH,y)],[pg.Vector2(x,0),pg.Vector2(x,_HEIGHT)]]
            # linha do mouse debug
            pg.display.flip()
            clock = self.clock.tick(60)
            pg.display.set_caption(str(clock))

            
             
        
             # para usar yield precisa chamar a função no  __init__
            pg.display.update()
            
            
            
if __name__ == "__main__":
    run = Random_Short([1,4,3,2])
    app = Game()
    app.run()
    pg.quit()
