import pygame
from obj import Obj

class Menu:
    def __init__(self):

        self.background = Obj('MENUTESTE/assets/Rota de Fuga.png',0,0)
        self.change_scene = False

    def draw(self,window):
        self.background.draw(window)
    
    def events(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True

