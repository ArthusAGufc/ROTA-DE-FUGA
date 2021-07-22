import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura = 500
largura = 640

x_pac = 0
y_pac = 0

x_coin = randint(50, 600)
y_coin = randint(50, 450)

fonte = pygame.font.SysFont("PixelMix", 40, True, True)

points = 0
#CRIANDO A JANELA
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rota de Fuga")
relogio = pygame.time.Clock()

#CRIANDO OS OBJETOS
while True:
    relogio.tick(400)
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {points}"
    texto = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_a]:
            x_pac = x_pac - 10
        if pygame.key.get_pressed()[K_d]:
            x_pac = x_pac + 10
        if pygame.key.get_pressed()[K_w]:
            y_pac = y_pac - 10
        if pygame.key.get_pressed()[K_s]:
            y_pac = y_pac + 10

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
    tela.blit(texto, (400, 50))

    if pacman.colliderect(linha_esq):
        x_pac = x_pac + 10
    if pacman.colliderect(linha_dir):
        x_pac = x_pac - 10
    if pacman.colliderect(linha_sup):
        y_pac = y_pac + 10
    if pacman.colliderect(linha_inf):
        y_pac = y_pac - 10

    pygame.display.update()


