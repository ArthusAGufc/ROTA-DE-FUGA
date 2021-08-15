import pygame
from menu import Menu
from game import Game

Speed = 2
class Main:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu()
        self.game = Game()

        self.loop = True
        
    def draw(self):
        self.window.fill([0,0,0])
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            self.menu.events(events)

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()


game = Main(1280, 720, "Rota de Fuga")
game.update()
