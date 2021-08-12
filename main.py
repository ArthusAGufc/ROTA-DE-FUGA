import pygame
from pygame.locals import *
from sys import exit
from random import randint

largura= 1000
altura= 400
Speed= 10

class Nave(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('Imagens/Nave.png')]
        self.atual = 0
        self.image = self.image_run[self.atual]
        self.image = pygame.transform.scale(self.image, (309//4, 163//4))

        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 160

    def update(self):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.rect[1] -= Speed
            if key[pygame.K_s]:
                self.rect[1] += Speed
            if key[pygame.K_d]:
                self.rect[0] += Speed
            if key[pygame.K_a]:
                self.rect[0] -= Speed

        move_player(self)

class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagens/Asteroide-2.png')
        self.image=pygame.transform.scale(self.image,(232//2,217//2))

        self.rect = self.image.get_rect()
        self.rect.topleft= 1000, randint(0, 400)

    def update(self):
        self.rect[0] -= Speed
        if self.rect[0] <- 150:
            self.rect.topleft = 1000, randint(0, 400)

Nave_Sprites= pygame.sprite.Group()
nave=Nave()
Nave_Sprites.add(nave)

Asteroide_Sprites= pygame.sprite.Group()
asteroide=Asteroide()
Asteroide_Sprites.add(asteroide)

#Iniciando o Pygame
pygame.init()

#Música de Fundo
pygame.mixer.music.set_volume(0.15)
musica = pygame.mixer.music.load('Músicas/Snes.mp3')
pygame.mixer.music.play(-1)

#Criando Janela
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Rota de Fuga')
background=pygame.image.load('Imagens/Universo.jpg')
background=pygame.transform.scale(background,(largura,altura))

clock=pygame.time.Clock()

while True:
    clock.tick(25)
    tela.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    Nave_Sprites.draw(tela)
    Asteroide_Sprites.draw(tela)

    Nave_Sprites.update()
    Asteroide_Sprites.update()

    pygame.display.update()
