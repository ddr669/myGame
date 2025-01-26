import pygame as pg

class Notepad:
    def __init__(self, height=800, width=580):
        self.H = height
        self.W = width
        pg.init()
        pg.font.init()
        self.running = True
        self._screen = pg.display.set_mode((self.W, self.H))
        self.screen = pg.Surface((self.W,self.H))
        self.clock = pg.time.Clock()
        
    def write(self, text="Hello,World!"):
        fonte = pg.font.SysFont("SmallFonts", size=24)
        escrita = fonte.render(text,False,(255,255,255))
        return escrita
    def escrever_arquivo(self, arqv=None, string="Hello,World!"):
        if arqv:
            
            with open(arqv, "a") as A:
                A.write(string+"\n")
        else:
            arqv = "new_text.txt"
            self.escrever_arquivo(arqv, string)
        
    def run(self):
        alp = ["a","b","c","d","e","f","g","h","i","j","k","l"] #,"","","","","","","","","","","","","","","","",""]
        while self.running:
            self.screen.fill((80,20,140))
            keys = pg.key.get_pressed()
            #string =  Verificar_Teclas(teclas)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            if keys[pg.K_a]:
                # Escrever_No_texto(arquivo, string)
                self.escrever_arquivo()
                self.screen.blit(self.write(text="a"), (0,0))
               # if keys[ord(w)]:
              #     text = self.write()
                 #  self._screen.blit(text, (100,100))
            #self.screen.fill(("black"))
            self._screen.blit(self.screen, (0,0))
            pg.display.flip()
            dt = self.clock.tick(60)
            

if __name__ == "__main__":
    app = Notepad()
    app.run()
