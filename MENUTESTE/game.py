from obj import Obj

class Game:
    def __init__(self):
        self.background = Obj('MENUTESTE/assets/Rota de Fuga.png',0,0)

        self.change_scene = False

    def draw(self,window):
        self.background.draw(window)
    
    def update(self):
        self.background.sprite.rect[0] += -5

        if self.background.sprite.rect[0] >= 720:
            self.background.sprite.rect[0] = 0

