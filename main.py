import pygame
from pygame.locals import *
from sys import exit

largura= 1000
altura= 400
Speed= 10

class Nave(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run=[pygame.image.load('Imagens/Nave.png')]
        self.atual = 0
        self.image= self.image_run[self.atual]
        self.image=pygame.transform.scale(self.image,(309//4,163//4))

        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 160

    def update(self,*args):
        def move_player(self):
            key=pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.rect[1] -= Speed
            if key[pygame.K_s]:
                self.rect[1] += Speed
            if key[pygame.K_d]:
                self.rect[0] += Speed
            if key[pygame.K_a]:
                self.rect[0] -= Speed
            self.image = pygame.transform.scale(self.image, [309//4,163//4])
        move_player(self)

todas_as_sprites= pygame.sprite.Group()
nave=Nave()
todas_as_sprites.add(nave)

pygame.init()

pygame.mixer.music.set_volume(0.12)
musica=pygame.mixer.music.load('Músicas/Snes.mp3')
pygame.mixer.music.play(-1)

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
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.update()
