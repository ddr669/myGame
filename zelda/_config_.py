from numpy import asarray as ARRAY



_HEIGHT = 720
_WIDTH = 1024

_CENTER = _HEIGHT /2, _WIDTH/2

_PLAYER = ARRAY( [[0,1], [0,0],[1,0],[1,1]] )

_R = 60 # 120
_G = 20 # 100
_B = 100 # 244
LISTA = []


def convertHEX(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"

def gradient(r=True, g=False, b=False,y=False, p=False,  ini=0, end=60):
        out = []
        if b:
            cc = ini
            for a in range(ini, end):
                out.append(convertHEX(ini,ini,a))
                cc += 1
            return out
        
        if g:
            cc = 0
            for a in range(ini, end):
                out.append(convertHEX(ini,a,ini))
                cc += 1
            return out
        if r:
            cc = 0
            for a in range(ini, end):
                out.append(convertHEX(a,ini,ini))
                cc += 1
            return out
        if y:
            for a in range(ini, end):
                out.append(convertHEX(a,a,ini))
            return out
        if p:
            for a in range(ini, end):
                out.append(convertHEX(a, ini, a))
            return out

    
     # if b:
        #    cc = 0
          #  for a in range(ini, end):
            #    out.append(convertHEX(r,g+cc,a))
              #  cc += 1
            #return out
        #else:
          #  if r:
            #    cc = 0
              #  for a in range(ini, end):
                #    out.append(convertHEX(a,g,b+cc))
             #       cc += 1
              #  return out
           # else:
              #  cc = 0
               # for a in range(ini, end):
                 #   out.append(convertHEX(r+cc,a,b))
                  #  cc += 1
                #return out""""



