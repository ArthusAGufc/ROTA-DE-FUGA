import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()


altura = 500
largura = 640

x_pac = 0
y_pac = 0

pac_movex = 0
pac_movey = 0

x_coin = randint(50, 600)
y_coin = randint(50, 450)

fonte = pygame.font.SysFont("PixelMix", 40, True, True)

points = 0
#CRIANDO A JANELA
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rota de Fuga")
relogio = pygame.time.Clock()

while True:
    relogio.tick(400)
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {points}"
    texto = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                pac_movex = -0.5
                pac_movey = 0
                x_pac = x_pac - pac_movex
            if event.key == K_d:
                pac_movex = 0.5
                pac_movey = 0
                x_pac = x_pac + pac_movex
            if event.key == K_w:
                pac_movey = -0.5
                pac_movex = 0
                y_pac = y_pac - pac_movey
            if event.key == K_s:
                pac_movey = 0.5
                pac_movex = 0
                y_pac = y_pac + pac_movey
    x_pac = x_pac + pac_movex
    y_pac = y_pac + pac_movey

#CRIANDO OBJETOS
    coin = pygame.draw.rect(tela, (255, 255, 255), (x_coin, y_coin, 10, 10))

    pacman = pygame.draw.rect(tela, (255, 255, 0), (x_pac, y_pac, 30, 30))

    linha_esq = pygame.draw.line(tela, (0, 0, 255), (0, 0), (0, 500), 10)
    linha_sup = pygame.draw.line(tela, (0, 0, 255), (0, 0), (640, 0), 10)
    linha_inf = pygame.draw.line(tela, (0, 0, 255), (0, 500), (640, 500), 10)
    linha_dir = pygame.draw.line(tela, (0, 0, 255), (640, 0), (640, 500), 10)

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

    pygame.display.update()

