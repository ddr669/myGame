import pygame as pg
import numpy as np
from numba import njit
class Game:    
    def __init__(self):
        self.angle = 0
        self.cor = "white"
        pg.init()
        self.WIDTH = 680
        self.HEIGHT = 420
        self.SCREEN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FOV_V = np.pi/4
        self.FOV_H = self.FOV_V*self.WIDTH/self.HEIGHT
        
        self.CAM = np.asarray([13,0.5,2,3.3,0])

        self.COCK = pg.time.Clock()
        self._running = True
 
        self.WHITE = "white"

        self.scale = 100/2

    def transparency(self, w=50, h=80, color=(0,0,0), alpha=0):
        surf = pg.Surface((w,h),pg.SRCALPHA)
        surf.fill((color[0],color[1],color[2], alpha))
        return surf
        
            
    def rota(self, screen, surf, pos, origPos, angle):
        img_rect = screen.get_rect(topleft=(pos[0]-origPos[0],pos[1]-origPos[1]))
        # 63 100
       
        
        offset_center = pg.math.Vector2(pos ) - img_rect.center

        rotated_offset = offset_center.rotate(-angle)

        rotated_img_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        rotated_img = pg.transform.rotate(screen,  angle)
        rotated_img_rect = rotated_img.get_rect(center=rotated_img_center)

        self.SCREEN.blit(rotated_img, rotated_img_rect)

        pg.draw.rect(screen, "white", (*rotated_img_rect.topleft, *rotated_img.get_size()),2)
        


    def _main(self):
        
        
       
        while self._running != False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self._running = False
            keys = pg.key.get_pressed()

            
            if pg.mouse.get_pressed()[0]:
                self.cor = "blue"
            else: self.cor="white"
                
            
            self.SCREEN.fill(("black"))
            scl = 1
            self.cube_()
            x_next = 10
            y_next = 0
            for b in  range(0, self.HEIGHT, 10):
                for a in range(0, self.WIDTH, 10):  
                    self.cube_(pos=(a,y_next))
                y_next += 10
 
           # pg.transform.rotate(surf, 90)
    

            
            
            pg.display.flip()
            if keys[pg.K_a]:
                self.angle += 1
            if keys[pg.K_d]:
                self.angle -= 1
            
            
            dt = self.COCK.tick(60) / 100
            pg.display.set_caption("[fps: "+ str(dt)+" ]")
    def cube_(self, pos = (0,0)):
        scl = 1
        w,h = self.WIDTH/2,self.HEIGHT/2
        lista = [pg.Vector2(1*scl,10*scl), pg.Vector2(10*scl, 10*scl),
                     pg.Vector2(1*scl,1*scl)]#,#pg.Vector2(1*scl,10*scl)]#, pg.Vector2(2*scl,2*scl),
                     #pg.Vector2(4*scl,4*scl)]
        lista1 = [pg.Vector2(10*scl,10*scl), pg.Vector2(1*scl,1*scl), pg.Vector2(10*scl , 1*scl)]
           
        surf2 = self.transparency(w=15,h=15)
            
        surf = self.transparency(w=15,h=15)
        trig1 = pg.draw.polygon(surf, "white", lista,0)
            
        trig2 = pg.draw.polygon(surf2, self.cor, lista1,0)#, "white" )
        pos2 =( pos[0],pos[1])
        self.rota(surf, trig1, pos, (0,0), self.angle)
        self.rota(surf2, trig2, pos2, (0,0), self.angle)
            

    def projection(self, camera, points):
        for point in points:
            h_angle_camera = np.arctan((point[2]-camera[2])/(point[0]-camera[0] + 1e-16))
            if abs(camera[0]+np.cos(h_angle_camera)-point[0]) > abs(camera[0]-point[0]):
                h_angle_camera = (h_angle_camera - np.pi)%(2*np.pi)
    def listo_vector_(self, *obj):
        lista = []
        for a in range(0, len(obj)):
            for b in range(0, len(obj[a])):
                for c in range(0,len(obj[a][b])):
                    
                    lista.append(int(obj[a][b][c]))
                    
        return lista
                  


if __name__ == "__main__":
    app = Game()
    app._main()
    pg.quit()
    
