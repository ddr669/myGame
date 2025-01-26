import pygame as pg
import numpy as np
from time import sleep

class Game:
    def pula(self, *player_pos):
        for anima in range(0, 10):
            for a in range(0, 4):
                self.player[a][1] -= 10
                
               
    def transparency(self, w, h, color=(0,0,0), alpha=0):
        surf = pg.Surface((w,h),pg.SRCALPHA)
        surf.fill((color[0], color[1], color[2], alpha))
        return surf 

    
    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 420
        self.screen = pg.display.set_mode((self.width, self.height))
        self.player  = [[20,420], [60,420], [60,380], [20,380]]
        self.clock = pg.time.Clock()
        self.running = True


    def __main__(self):
        while self.running != False:
            self.screen.fill("black")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.pula(self.player)
           
            
            pg.draw.polygon(self.screen, "green", self.player)
            print(self.player)

            
            pg.display.update()
            pg.display.flip()
            dt = self.clock.tick(6)/100
            pg.display.set_caption(str(dt))

if __name__ == "__main__":
    app = Game()
    app.__main__()
    pg.quit()
            
            
            
