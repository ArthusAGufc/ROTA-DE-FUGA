import pygame, random
Speed = 10
largura= 1000
altura= 400

pipe_largura = 500#largura do pilar
pipe_altura = 500#altura do pilar
pipe_espaco = 35#espaço entre os pilares

class Pipe(pygame.sprite.Sprite):  # cria 'canos'

    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Imagens/pipes.png').convert_alpha()  # aloca uma imagem
        self.image = pygame.transform.scale(self.image, (pipe_largura, pipe_altura))  # redimensiona a imagem

        self.rect = self.image.get_rect()  # cria uma colisão
        self.rect[0] = xpos

        if inverted:  # se o cano tiver invertido
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.rect[1] = altura - ysize
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= Speed  # velocidade dos canos