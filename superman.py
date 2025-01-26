

from random import randint

class Dado:
    def __init__(self) -> int :
        self.n = randint(0, 6)
        
    

class Player1(Dado):
    def __init__(self) -> None:
        dado = super().__init__()
        self.main()
    def main(self)->int:return self.n
    
class Player2(Dado):
    def __init__(self) -> None:
        dado = super().__init__()
        self.main()
        
    def main(self)->int:return self.n

class Jogo(Player1, Player2):
    def __init__(self):
        super().__init__()
        self.main()
    
        
        
