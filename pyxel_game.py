import pyxel

pyxel.init(1200, 900)
play = {
    "x": 1200/2,
    "y": 900/2
    }
e = 0
z = 0
"""fase1 = {
    1: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    2: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    3: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    4: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    5: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    6: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    7: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    8: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}],
    9: [{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":},{"x1":,"y1":,"x2":,"y2":}]
    }
"""
TT = [[]]
player_pos = [0,0]
def update():
    global e
    global player_pos
    global z
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_A):
        player_pos[0] -= 50
    if pyxel.btnp(pyxel.KEY_W):
        z -= 50
    if pyxel.btnp(pyxel.KEY_S):
        z += 50
    if pyxel.btnp(pyxel.KEY_D):
        player_pos[0] += 50

 
def draw():
    pyxel.cls(0)
              # localização | tamanho| cor
              #x , y,       | x, y,  |
              # pyxel.rect()
    
    pyxel.rect(0, 0, 1200, 900, 0)
    # background
    pyxel.camera(player_pos[0],player_pos[1])
    
    pyxel.line(300,900,300,0,25)
    pyxel.line(600,900,600,0,25)
    pyxel.line(1800,900,1800,0,25)

    
    #pyxel.rect(10, 10, 10, 880, 0)
    # linha de cima
    #pyxel.rect(1180, 10, 10, 880, 0)
    # linha da direita
    #pyxel.rect(10, 10, 1180, 10, 0)
    # linha da esquerda
    #pyxel.rect(10, 880, 1180, 10, 0)
    # linha de baixo
    ###################################
    #for i in range(0, e):
    #   pyxel.rect(TT[i][0], TT[i][1], TT[i][2], TT[i][3], TT[i][4])

    ###################################
    #pyxel.rect(play["x"],play["y"], 20, 20, 8)

pyxel.run(update, draw)
