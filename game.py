import pygame
from random import randint
import numpy as np

mapa = [
    
    ]
# pygame setup
pygame.init()
screen = pygame.display.set_mode((440, 220))
clock = pygame.time.Clock()
running = True
dt = 0
             #      x, y

player_pos = [pygame.Vector2(0,200),pygame.Vector2(440,200)]
parede = [[pygame.Vector2(0,0),pygame.Vector2(60,30)]
          ,[pygame.Vector2(0,220),pygame.Vector2(60,220-30)]
          ,[pygame.Vector2(440,0),pygame.Vector2(440-60,30)]
          ,[pygame.Vector2(440,220),pygame.Vector2(440-60,220-30)]
          ,[pygame.Vector2()]]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.draw.line(screen, "white", player_pos[0],player_pos[1])
    
    #pygame.draw.circle(screen, "green", pygame.Vector2(40/2,180/2), 8/2)
    #pygame.draw.circle(screen, "green", pygame.Vector2(80/2,120/2), 4/2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pass 
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_a]:
        player_pos[0][0] += 20
        player_pos[0][1] += 5
        player_pos[1][1] -= 5
    if keys[pygame.K_d]:
        player_pos[0][1] -= 20
        player_pos[1][0] -= 5
        player_pos[1][1] += 5
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 100
    a = str(player_pos[0][0]),str(player_pos[0][1]),str(player_pos[1][0]),str(player_pos[1][1])    
    pygame.display.set_caption(str(a))    
pygame.quit()
