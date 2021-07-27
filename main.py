import pygame
from pygame.locals import *
from sys import exit
from random import randint
#from pygame.image import load

pygame.init()

class Freeze(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprite_00.png"))
        self.sprites.append(pygame.image.load("data/sprite_02.png"))
        self.sprites.append(pygame.image.load("data/sprite_03.png"))
        self.sprites.append(pygame.image.load("data/sprite_05.png"))
        self.sprites.append(pygame.image.load("data/sprite_06.png"))
        self.sprites.append(pygame.image.load("data/sprite_07.png"))
        self.sprites.append(pygame.image.load("data/sprite_09.png"))
        self.sprites.append(pygame.image.load("data/sprite_10.png"))
        self.sprites.append(pygame.image.load("data/sprite_13.png"))
        self.sprites.append(pygame.image.load("data/sprite_14.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

todas_as_sprites = pygame.sprite.Group()
freeze = Freeze()
todas_as_sprites.add(freeze)


altura = 650
largura = 1300

x_pac = 0
y_pac = 0

pac_movex = 0
pac_movey = 0
speed_pac = 0.7

x_coin = randint(50, 600)
y_coin = randint(50, 450)

fonte = pygame.font.SysFont("PixelMix", 40, True, True)

points = 0
#CRIANDO A JANELA
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rota de Fuga")
relogio = pygame.time.Clock()
#background = load('Imagem_a_ser_colocada.png')

while True:
    relogio.tick(400)
    tela.fill((0, 0, 0)) #substituir tla.fill por tela.blit(background, (0, 0))
    mensagem = f"Pontos: {points}"
    texto = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                pac_movex = -speed_pac
                pac_movey = 0
                x_pac = x_pac - pac_movex
            if event.key == K_d:
                pac_movex = speed_pac
                pac_movey = 0
                x_pac = x_pac + pac_movex
            if event.key == K_w:
                pac_movey = -speed_pac
                pac_movex = 0
                y_pac = y_pac - pac_movey
            if event.key == K_s:
                pac_movey = speed_pac
                pac_movex = 0
                y_pac = y_pac + pac_movey
    x_pac = x_pac + pac_movex
    y_pac = y_pac + pac_movey

#CRIANDO OBJETOS
    coin = pygame.draw.rect(tela, (255, 255, 255), (x_coin, y_coin, 10, 10))

    pacman = pygame.draw.rect(tela, (255, 255, 0), (x_pac, y_pac, 30, 30))

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    linha_esq = pygame.draw.line(tela, (0, 0, 255), (0, 0), (0, 650), 20)
    linha_sup = pygame.draw.line(tela, (0, 0, 255), (0, 0), (1300, 0), 20)
    linha_inf = pygame.draw.line(tela, (0, 0, 255), (0, 650), (1300, 650), 20)
    linha_dir = pygame.draw.line(tela, (0, 0, 255), (1300, 0), (1300, 650), 20)

    if pacman.colliderect(coin):
        points = points + 1
        x_coin = randint(50, 600)
        y_coin = randint(50, 450)
    tela.blit(texto, (450, 30))

    if pacman.colliderect(linha_esq):
        x_pac = x_pac + 10
    if pacman.colliderect(linha_dir):
        x_pac = x_pac - 10
    if pacman.colliderect(linha_sup):
        y_pac = y_pac + 10
    if pacman.colliderect(linha_inf):
        y_pac = y_pac - 10

    pygame.display.flip()
