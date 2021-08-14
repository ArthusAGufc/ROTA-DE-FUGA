import pygame
from pygame.locals import *
from sys import exit

largura= 1000
altura= 400
Speed= 10
Nave_Speed=7

#Criando Nave
class Nave(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[]
        self.sprites.append(pygame.image.load('Imagens/sprite_0.png'))
        self.sprites.append(pygame.image.load('Imagens/sprite_1.png'))
        self.sprites.append(pygame.image.load('Imagens/sprite_2.png'))
        self.atual = 0
        self.image= self.sprites[self.atual]
        self.image=pygame.transform.scale(self.image,(5253//60,2771//60))

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = 50, 160

    def update(self):
        self.atual=self.atual+1
        if self.atual>=len(self.sprites):
            self.atual=0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (5253 // 60, 2771 // 60))

        def move_player(self):
            key=pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.rect[1] -= Nave_Speed
            if key[pygame.K_s]:
                self.rect[1] += Nave_Speed
            if key[pygame.K_d]:
                self.rect[0] += Nave_Speed
            if key[pygame.K_a]:
                self.rect[0] -= Nave_Speed
        move_player(self)

    def movimento(self):
        if self.rect.x<=0:
            self.rect.x=0
        if self.rect.x>=915:
            self.rect.x=915
        if self.rect.y<=0:
            self.rect.y=0
        if self.rect.y>=355:
            self.rect.y=355

#Criando Asteroides
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagens/Asteroide-2.png')
        self.image=pygame.transform.scale(self.image,(232//2,217//2))

        self.rect=self.image.get_rect()
        self.rect.topleft= 1000,0

    def update(self):
        self.rect[0] -= Speed
        if self.rect[0]<-150:
            self.rect.topleft = 1000,0

class Obstaculo2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagens/Asteroide-2.png')
        self.image=pygame.transform.scale(self.image,(232//2,217//2))

        self.rect=self.image.get_rect()
        self.rect.topleft= 1200,150

    def update(self):
        self.rect[0] -= Speed
        if self.rect[0]<-150:
            self.rect.topleft = 1200,150

class Obstaculo3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagens/Asteroide-2.png')
        self.image=pygame.transform.scale(self.image,(232//2,217//2))

        self.rect=self.image.get_rect()
        self.rect.topleft= 1100,300

    def update(self):
        self.rect[0] -= Speed
        if self.rect[0]<-150:
            self.rect.topleft = 1100,300

#Criando Moeda
class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Imagens/Moeda.png')
        self.image = pygame.transform.scale(self.image, (555 // 8, 449 // 8))

        self.rect = self.image.get_rect()
        self.rect.topleft = 1500, 300
    def update(self):
        self.rect[0] -= Speed
        if self.rect[0]<-150:
            self.rect.topleft = 1500,300

Nave_Sprites= pygame.sprite.Group()
nave=Nave()
Nave_Sprites.add(nave)

Moeda_Sprites=pygame.sprite.Group()
Moeda_Sprites.add(Moeda())

Obstaculo_Sprites= pygame.sprite.Group()
Obstaculo_Sprites.add(Obstaculo())
Obstaculo_Sprites.add(Obstaculo2())
Obstaculo_Sprites.add(Obstaculo3())

#Iniciando o Pygame
pygame.init()

#Música de Fundo
pygame.mixer.music.load('Músicas/Snes.mp3')
pygame.mixer.music.play(-1)

#Pontuação
fonte_pontos=pygame.font.SysFont('arial', 30, True, True)
fonte_perdeu=pygame.font.SysFont('arial', 50, True, True)
pontos=0

#Criando Janela
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Rota de Fuga')
background=pygame.image.load('Imagens/Universo.jpg')
background=pygame.transform.scale(background,(largura,altura))

clock=pygame.time.Clock()

def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    paused=False

while True:
    nave.movimento()
    clock.tick(80)
    tela.blit(background, (0, 0))

    mensagem=f'Pontos: {pontos}'
    Mensagem='Game Over'
    texto_perdeu=fonte_perdeu.render(Mensagem, True, (0, 0, 0))
    texto_formatado = fonte_pontos.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_p:
                pause()
            elif event.key==K_q:
                pygame.quit()
                quit()

    tela.blit(texto_formatado, (830, 0))
    colisoes=pygame.sprite.spritecollide(nave,Obstaculo_Sprites,False,pygame.sprite.collide_mask)
    Nave_Sprites.draw(tela)
    Obstaculo_Sprites.draw(tela)
    Moeda_Sprites.draw(tela)

    if colisoes:
        pass
        musica = pygame.mixer.music.load('Músicas/Snes.mp3')
        pygame.mixer.pause()
        tela.blit(texto_perdeu, (400, 175))
    else:
        Nave_Sprites.update()
        Obstaculo_Sprites.update()
        Moeda_Sprites.update()

    pygame.display.update()
