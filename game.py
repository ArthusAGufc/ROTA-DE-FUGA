# Importações
import pygame_menu
import pygame
import random
from pygame.locals import *
from pipes import *
from random import randrange

# Configurações das Pipes
Speed = 10
largura= 1000
altura= 400

pipe_largura = 500 # largura do pilar
pipe_altura = 500 # altura do pilar
pipe_espaco = 35 # espaço entre os pilares

# Configurações da Nave
sprite1 = pygame.image.load('Naves/Naves_TER/Nave Fup/NaveFup_0.png')
sprite2 = pygame.image.load('Naves/Naves_TER/Nave Fup/NaveFup_1.png')
sprite3 = pygame.image.load('Naves/Naves_TER/Nave Fup/NaveFup_2.png')
largura = 1000
altura = 400
Obstaculos_Speed = 13
Nave_Speed = 8
sprites = [sprite1, sprite2, sprite3]

# Inicio do Jogo Pygame
pygame.init()

def controles():
    # Criação da Janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Menu/Mapa-2.jpg')
    background = pygame.transform.scale(background, (largura, altura))

    retangulo = pygame.image.load('Menu/retangulo.png')
    retangulo = pygame.transform.scale(retangulo, (225 // 1, 225 // 4))

    # Fonte do Texto do Jogo
    Fonte_Controles = pygame.font.SysFont('arial', 50, True, True)
    Fonte_Texto = pygame.font.SysFont('arial', 20, True, True)

    while True:
        # Imagens
        tela.blit(background, (0, 0))
        tela.blit(retangulo, (300, 35))
        tela.blit(retangulo, (300, 85))
        tela.blit(retangulo, (300, 135))
        tela.blit(retangulo, (300, 185))
        tela.blit(retangulo, (300, 235))
        tela.blit(retangulo, (300, 285))
        tela.blit(retangulo, (300, 335))

        # Texto sobre controles do código
        Texto_Controles = Fonte_Controles.render('Controles', True, (255, 255, 255))
        Texto_W = Fonte_Texto.render('Mover Para Cima', True, (255, 255, 255))
        Texto_S = Fonte_Texto.render('Mover Para Baixo', True, (255, 255, 255))
        Texto_A = Fonte_Texto.render('Mover Para Esquerda', True, (255, 255, 255))
        Texto_D = Fonte_Texto.render('Mover Para Direita', True, (255, 255, 255))
        Texto_Pausar = Fonte_Texto.render('Pausar Jogo', True, (255, 255, 255))
        Texto_Sair = Fonte_Texto.render('Sair do Jogo', True, (255, 255, 255))
        Texto_Retornar = Fonte_Texto.render('Retornar', True, (255, 255, 255))
        Tecla_W = Fonte_Texto.render('W', True, (255, 255, 255))
        Tecla_S = Fonte_Texto.render('S', True, (255, 255, 255))
        Tecla_A = Fonte_Texto.render('A', True, (255, 255, 255))
        Tecla_D = Fonte_Texto.render('D', True, (255, 255, 255))
        Tecla_P = Fonte_Texto.render('P', True, (255, 255, 255))
        Tecla_Q = Fonte_Texto.render('Q', True, (255, 255, 255))
        Tecla_BackSpace = Fonte_Texto.render('BackSpace', True, (255, 255, 255))

        # Medida do Retangulo onde esta o texto
        tela.blit(Texto_Controles, (largura // 2.5, -10))
        tela.blit(Texto_W, (50, 50))
        tela.blit(Texto_S, (50, 100))
        tela.blit(Texto_A, (50, 150))
        tela.blit(Texto_D, (50, 200))
        tela.blit(Texto_Pausar, (50, 250))
        tela.blit(Texto_Sair, (50, 300))
        tela.blit(Texto_Retornar, (50, 350))
        tela.blit(Tecla_W, (400, 50))
        tela.blit(Tecla_S, (400, 100))
        tela.blit(Tecla_A, (400, 150))
        tela.blit(Tecla_D, (400, 200))
        tela.blit(Tecla_P, (400, 250))
        tela.blit(Tecla_Q, (400, 300))
        tela.blit(Tecla_BackSpace, (360, 350))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    menu()

        pygame.display.update()

def historia():
    # Música da História
    #pygame.mixer.music.set_volume(0.5)
    #pygame.mixer.music.load('Músicas/StarWars.mp3')
    #pygame.mixer.music.play(2)

    # História
    class Historia1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-1.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 0

        def update(self):
            self.rect[1] -= 1

    class Historia2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-2.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 400

        def update(self):
            self.rect[1] -= 1

    class Historia3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-3.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 900

        def update(self):
            self.rect[1] -= 1

    class Historia4(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/PeterCaleb-1.png')
            self.image = pygame.transform.scale(self.image, (500, 500 // 2))

            self.rect = self.image.get_rect()
            self.rect.topleft = 250, 1300

        def update(self):
            self.rect[1] -= 1

    class Historia5(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-4.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 1700

        def update(self):
            self.rect[1] -= 1

    class Historia6(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/Darktrol.jpg')
            self.image = pygame.transform.scale(self.image, (500, 500 // 2))

            self.rect = self.image.get_rect()
            self.rect.topleft = 250, 2100

        def update(self):
            self.rect[1] -= 1

    class Historia7(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-5.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 2300

        def update(self):
            self.rect[1] -= 1

    class Historia8(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/Joe Trump.png')
            self.image = pygame.transform.scale(self.image, (500, 500 // 2))

            self.rect = self.image.get_rect()
            self.rect.topleft = 250, 2700

        def update(self):
            self.rect[1] -= 1

    class Historia9(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-6.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 3000

        def update(self):
            self.rect[1] -= 1

    class Historia10(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/Guerra-1.png')
            self.image = pygame.transform.scale(self.image, (500, 500 // 2))

            self.rect = self.image.get_rect()
            self.rect.topleft = 250, 3400

        def update(self):
            self.rect[1] -= 1

    class Historia11(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/Guerra-2.png')
            self.image = pygame.transform.scale(self.image, (500, 500 // 2))

            self.rect = self.image.get_rect()
            self.rect.topleft = 250, 3700

        def update(self):
            self.rect[1] -= 1

    class Historia12(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Historia/História-7.png')
            self.image = pygame.transform.scale(self.image, (largura, altura))

            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 4000

        def update(self):
            self.rect[1] -= 1

    # Imagens da História
    Historia_Sprites = pygame.sprite.Group()
    Historia_Sprites.add(Historia1())
    Historia_Sprites.add(Historia2())
    Historia_Sprites.add(Historia3())
    Historia_Sprites.add(Historia4())
    Historia_Sprites.add(Historia5())
    Historia_Sprites.add(Historia6())
    Historia_Sprites.add(Historia7())
    Historia_Sprites.add(Historia8())
    Historia_Sprites.add(Historia9())
    Historia_Sprites.add(Historia10())
    Historia_Sprites.add(Historia11())
    Historia_Sprites.add(Historia12())

    # Janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Menu/Mapa-2.jpg')
    background = pygame.transform.scale(background, (largura, altura))
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        tela.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    #pygame.mixer.music.load('Músicas/StarWars.mp3')
                    #pygame.mixer.music.pause()
                    menu()

        Historia_Sprites.draw(tela)
        Historia_Sprites.update()

        pygame.display.update()

def creditos():
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Menu/Mapa-2.jpg')
    background = pygame.transform.scale(background, (largura, altura))

    # Logo da Equípe
    class ShadowDemons(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Menu/Shadow Demons.png')
            self.image = pygame.transform.scale(self.image, (550, 550))

            self.rect = self.image.get_rect()
            self.rect.topleft = 900, -50

        def update(self):
            self.rect[0] -= 1
            if self.rect.x <= 500:
                self.rect.x = 500

    ShadowDemons_Sprites = pygame.sprite.Group()
    ShadowDemons_Sprites.add(ShadowDemons())

    # Fonte
    Fonte_Creditos = pygame.font.SysFont('arial', 40, True, True)
    Fonte_Integrantes = pygame.font.SysFont('arial', 25, True, True)

    while True:
        tela.blit(background, (0, 0))

        # Texto
        Texto_Creditos = Fonte_Creditos.render('Créditos', True, (255, 255, 255))
        Texto_Integrante1 = Fonte_Integrantes.render('ARTHUS ALMEIDA GIRAO', True, (255, 255, 255))
        Texto_Integrante2 = Fonte_Integrantes.render('GABRIEL NOVAIS LIMA', True, (255, 255, 255))
        Texto_Integrante3 = Fonte_Integrantes.render('KAUAN DEYVID BEZERRA DE SOUSA', True, (255, 255, 255))
        Texto_Integrante4 = Fonte_Integrantes.render('MARCOS GABRIEL DE MESQUITA MAURICIO', True, (255, 255, 255))
        Texto_Integrante5 = Fonte_Integrantes.render('PAULO HENRIQUE DA SILVA HOLANDA', True, (255, 255, 255))
        Texto_Integrante6 = Fonte_Integrantes.render('Orientador: Rafael Ivo', True, (255, 255, 255))
        Texto_Equipe = Fonte_Creditos.render('Shadow Demons', True, (255, 255, 255))

        # Imagem
        tela.blit(Texto_Creditos, (200, 0))
        tela.blit(Texto_Integrante1, (120, 50))
        tela.blit(Texto_Integrante2, (130, 100))
        tela.blit(Texto_Integrante3, (50, 150))
        tela.blit(Texto_Integrante4, (10, 200))
        tela.blit(Texto_Integrante5, (50, 250))
        tela.blit(Texto_Integrante6, (130, 300))
        tela.blit(Texto_Equipe, (600, 300))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    menu()

        ShadowDemons_Sprites.draw(tela)
        ShadowDemons_Sprites.update()

        pygame.display.update()

def github():
    tela = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Rota de Fuga')

    font = pygame_menu.font.FONT_NEVIS
    mybackground = pygame_menu.baseimage.BaseImage(image_path='Menu/Mapa-2.jpg',
                                                   drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    mytheme = pygame_menu.themes.THEME_DARK.copy()
    mytheme.widget_font = font
    mytheme.background_color = mybackground
    mytheme.title_font_shadow = True
    mytheme.widget_padding = 8
    mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE

    GitHub = pygame_menu.Menu(title='Rota de Fuga', width=1000, height=400, theme=mytheme)

    GitHub.add.url('https://github.com/ArthusAGufc/ROTA-DE-FUGA', font_color=pygame.Color(255, 255, 255))
    GitHub.add.url('https://github.com/ArthusAGufc/ROTA-DE-FUGA', 'Rota de Fuga Documentation',
                   font_color=pygame.Color(255, 255, 255))
    GitHub.add.button('Sair', menu)
    GitHub.mainloop(tela)

def loja():
    tela = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Rota de Fuga')

    font = pygame_menu.font.FONT_8BIT
    mybackground = pygame_menu.baseimage.BaseImage(image_path='Menu/Mapa-2.jpg',
                                                   drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    mytheme = pygame_menu.themes.THEME_DARK.copy()
    mytheme.widget_font = font
    mytheme.background_color = mybackground
    mytheme.title_font_shadow = True
    mytheme.widget_padding = 8
    mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE

    Loja = pygame_menu.Menu(title='Loja', width=1000, height=400, theme=mytheme)

    Loja.add.button('Naves Ter', NavesTER)
    Loja.add.button('Naves Dark', NavesDARK)
    Loja.add.button('Sair', menu)
    Loja.mainloop(tela)

def NavesTER():
    tela = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Rota de Fuga')
    fundo_da_loja = pygame.image.load('Lojas_Ter_Dark/TER/1NEW.jpg')
    fundo_da_loja2 = pygame.image.load('Lojas_Ter_Dark/TER/2NEW.jpg')
    fundo_da_loja3 = pygame.image.load('Lojas_Ter_Dark/TER/3NEW.jpg')
    fundo_da_loja4 = pygame.image.load('Lojas_Ter_Dark/TER/4NEW.jpg')
    fundo_da_loja5 = pygame.image.load('Lojas_Ter_Dark/TER/5NEW.jpg')
    fundo_da_loja6 = pygame.image.load('Lojas_Ter_Dark/TER/6NEW.jpg')
    Fonte_Texto1 = pygame.font.SysFont('arial', 30, True, True)
    file = open('maxcoin.txt', 'r')
    maxcoin = file.read()

    while True:
        Texto_MaxCoin = Fonte_Texto1.render(f'Moedas: {maxcoin}', True, (255, 255, 255))
        Texto_Voltar = Fonte_Texto1.render(f'Pressione Backspace Para Voltar', True, (255, 255, 255))
        pos = pygame.mouse.get_pos()  # indentifica a posição do mouse dentro da loja
        click = pygame.mouse.get_pressed()  # indentifica quando o mause pressionado

        if int(maxcoin) < 100:
            tela.blit(fundo_da_loja, (0, 0))
        elif int(maxcoin)< 250:
            tela.blit(fundo_da_loja2, (0, 0))
        elif int(maxcoin) < 375:
            tela.blit(fundo_da_loja3, (0, 0))
        elif int(maxcoin) < 425:
            tela.blit(fundo_da_loja4, (0, 0))
        elif int(maxcoin) < 500:
            tela.blit(fundo_da_loja5, (0, 0))
        else:
            tela.blit(fundo_da_loja6, (0, 0))

        if 373 >= pos[1] >= 351 and 276 >= pos[0] >= 26 and int(maxcoin)>=100: # Nave Caçador
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_TER/Caçador/Caçador_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Caçador/Caçador_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Caçador/Caçador_2.png'))
        elif 373 >= pos[1] >= 351 and 627 >= pos[0] >= 378 and int(maxcoin)>=375: # Nave Azul
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Azul/NaveAzul_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Azul/NaveAzul_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Azul/NaveAzul_2.png'))
        elif 373 >= pos[1] >= 351 and 970 >= pos[0] >= 721 and int(maxcoin)>=500: # Nave Caça Branco
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_TER/Caça Branco/CaçaBranco_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Caça Branco/CaçaBranco_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Caça Branco/CaçaBranco_2.png'))            
        elif 184 >= pos[1] >= 159 and 276 >= pos[0] >= 26 and int(maxcoin)>0:  # Nave Fup
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Fup/NaveFup_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Fup/NaveFup_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Fup/NaveFup_2.png'))
        elif 184 >= pos[1] >= 159 and 627 >= pos[0] >= 378 and int(maxcoin)>=250: # Nave Corrida
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_TER/Corrida/Corrida_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Corrida/Corrida_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Corrida/Corrida_2.png'))
        elif 184 >= pos[1] >= 159 and 970 >= pos[0] >= 721 and int(maxcoin)>=425: # Nave Presidencial
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Presidencial/NavePresidente_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Presidencial/NavePresidente_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_TER/Nave Presidencial/NavePresidente_2.png'))
               

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    loja()

        tela.blit(Texto_MaxCoin, (750, 0))
        tela.blit(Texto_Voltar, (0, 0))

        pygame.display.update()

def NavesDARK():
    tela = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Rota de Fuga')
    fundo_da_loja = pygame.image.load('Lojas_Ter_Dark/DARK/1BOL.jpg')
    fundo_da_loja2 = pygame.image.load('Lojas_Ter_Dark/DARK/2BOL.jpg')
    fundo_da_loja3 = pygame.image.load('Lojas_Ter_Dark/DARK/3BOL.jpg')
    fundo_da_loja4 = pygame.image.load('Lojas_Ter_Dark/DARK/4BOL.jpg')
    fundo_da_loja5 = pygame.image.load('Lojas_Ter_Dark/DARK/5BOL.jpg')
    fundo_da_loja6 = pygame.image.load('Lojas_Ter_Dark/DARK/6BOL.jpg')
    Fonte_Texto1 = pygame.font.SysFont('arial', 30, True, True)
    file = open('maxcoin.txt', 'r')
    maxcoin = file.read()

    while True:
        Texto_MaxCoin = Fonte_Texto1.render(f'Moedas: {maxcoin}', True, (255, 255, 255))
        Texto_Voltar = Fonte_Texto1.render(f'Pressione Backspace Para Voltar', True, (255, 255, 255))
        pos = pygame.mouse.get_pos()  # indentifica a posição do mouse dentro da loja
        click = pygame.mouse.get_pressed()  # indentifica quando o mause pressionado

        if int(maxcoin) < 100:
            tela.blit(fundo_da_loja, (0, 0))
        elif int(maxcoin)< 250:
            tela.blit(fundo_da_loja2, (0, 0))
        elif int(maxcoin) < 375:
            tela.blit(fundo_da_loja3, (0, 0))
        elif int(maxcoin) < 425:
            tela.blit(fundo_da_loja4, (0, 0))
        elif int(maxcoin) < 500:
            tela.blit(fundo_da_loja5, (0, 0))
        else:
            tela.blit(fundo_da_loja6, (0, 0))

        if 373 >= pos[1] >= 351 and 276 >= pos[0] >= 26 and int(maxcoin)>=100: # Nave Velocirapido
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_DARK/Velocirapido/Velocirapido_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Velocirapido/Velocirapido_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Velocirapido/Velocirapido_2.png'))
        elif 373 >= pos[1] >= 351 and 627 >= pos[0] >= 378 and int(maxcoin)>=375: # Nave Batedor
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_DARK/Batedor/Batedor_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Batedor/Batedor_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Batedor/Batedor_2.png'))
        elif 373 >= pos[1] >= 351 and 970 >= pos[0] >= 721 and int(maxcoin)>=500: # Nave Destruidor
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_DARK/Destruidor/Destruidor_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Destruidor/Destruidor_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Destruidor/Destruidor_2.png'))
        elif 184 >= pos[1] >= 159 and 276 >= pos[0] >= 26 and int(maxcoin)>0:  # Nave Sabre
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_DARK/Sabre/Sabre_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Sabre/Sabre_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Sabre/Sabre_2.png'))
        elif 184 >= pos[1] >= 159 and 627 >= pos[0] >= 378 and int(maxcoin)>=250: # Nave ermelha
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_DARK/Vermelha/Vermelha_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Vermelha/Vermelha_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Vermelha/Vermelha_2.png'))
        elif 184 >= pos[1] >= 159 and 970 >= pos[0] >= 721 and int(maxcoin)>=425: # Nave Preta
            if click[0] == 1:
                sprites.clear()
                sprites.append(pygame.image.load('Naves/Naves_DARK/Preta/Preta_0.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Preta/Preta_1.png'))
                sprites.append(pygame.image.load('Naves/Naves_DARK/Preta/Preta_2.png'))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    loja()

        tela.blit(Texto_MaxCoin, (750, 0))
        tela.blit(Texto_Voltar, (0, 0))

        pygame.display.update()

def game():
    # Criando Nave
    class Nave(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.atual = 0
            self.image = sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (5253 // 60, 2771 // 60))

            self.rect = self.image.get_rect()
            self.rect.topleft = 50, 160

        def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(sprites):
                self.atual = 0
            self.image = sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (5253 // 60, 2771 // 60))

            def move_player(self):
                key = pygame.key.get_pressed()
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
            if self.rect.x <= 0:
                self.rect.x = 0
            if self.rect.x >= 915:
                self.rect.x = 915
            if self.rect.y <= 0:
                self.rect.y = 0
            if self.rect.y >= 355:
                self.rect.y = 355
            


    # Mudança de Naves
    Nave_Sprites = pygame.sprite.Group()
    nave = Nave()
    Nave_Sprites.add(nave)

    # Criando Pipes
    class Pipe(pygame.sprite.Sprite):  # cria 'canos'

        def __init__(self, inverted, xpos, ysize):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/pipes.png').convert_alpha()  # aloca uma imagem
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


    def is_off_screen(sprite):  # se estiver fora da tela
        return sprite.rect[0] < -(sprite.rect[2])

    def get_random_pipes(xpos):  # gera canos aleatorios
        size = random.randint(-25, 310)  # gera canos de acordo com o valor atribuido
        pipe = Pipe(False, xpos, size)  # pipe normal
        pipe_inverted = Pipe(True, xpos, altura - size - pipe_espaco)  # pipe invertido
        return (pipe, pipe_inverted)

    # Criando Asteroides
    class Obstaculo(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/Asteroide-2.png')
            self.image = pygame.transform.scale(self.image, (232 // 2, 217 // 2))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 1200, 400)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 1200, 400)

    Asteroides_Sprites = pygame.sprite.Group()
    for i in range(3):
        Asteroides_Sprites.add(Obstaculo())

    # Criando Satellite
    class Satellite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/Satellite.png')
            self.image = pygame.transform.scale(self.image, (232 // 2, 217 // 2))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 1200, 400)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 1200, 400)

    Satellite_Sprites = pygame.sprite.Group()
    for i in range(3):
        Satellite_Sprites.add(Satellite())

    # Criando Planetas
    class Planeta1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/Mercurio.png')
            self.image = pygame.transform.scale(self.image, (232 // 2, 217 // 3))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 1200, 400)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 1200, 400)

    class Planeta2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/Saturno.png')
            self.image = pygame.transform.scale(self.image, (232 // 2, 217 // 2))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 1200, 400)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 1200, 400)

    class Planeta3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/Terra.png')
            self.image = pygame.transform.scale(self.image, (232 // 2, 217 // 2))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 1200, 400)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 1200, 400)

    class Planeta4(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Obstaculos/Netuno.png')
            self.image = pygame.transform.scale(self.image, (232 // 2, 217 // 2))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 1200, 400)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 1200, 400)

    Planetas_Sprites = pygame.sprite.Group()
    Planetas_Sprites.add(Planeta1())
    Planetas_Sprites.add(Planeta2())
    Planetas_Sprites.add(Planeta3())
    Planetas_Sprites.add(Planeta4())

    # Criando Moeda
    class Moeda(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Moedas/Fup_coin_1.png')
            self.image = pygame.transform.scale(self.image, (136 // 3, 123 // 3))

            self.rect = self.image.get_rect()
            self.rect.y = randrange(0, 400, 100)
            self.rect.x = largura + randrange(0, 400, 100)

        def update(self):
            self.rect[0] -= Obstaculos_Speed
            if self.rect[0] < -100:
                self.rect.y = randrange(0, 400, 100)
                self.rect.x = largura + randrange(0, 400, 100)

    Moeda_Sprites = pygame.sprite.Group()
    for i in range(3):
        Moeda_Sprites.add(Moeda())

    # Número de Gerações de Canos
    pipe_group = pygame.sprite.Group()  # Grupo de canos
    for i in range(2):  # gerar 2 canos por vez
        pipes = get_random_pipes(largura * i + 1000)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])
    """
    #Música de Fundo
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load('Músicas/Snes.mp3')
    pygame.mixer.music.play(-1)
    Coin=pygame.mixer.Sound('Músicas/Coin.mp3')
    Coin.set_volume(0.1)
    """
    # Texto
    Fonte_Texto1 = pygame.font.SysFont('arial', 30, True, True)
    Fonte_Texto2 = pygame.font.SysFont('arial', 50, True, True)

    # Pontuação
    coin = 0
    maxcoin = 0
    score = 0
    highscore = 0

    # Criando Janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Menu/Mapa-2.jpg')
    background = pygame.transform.scale(background, (largura, altura))
    clock = pygame.time.Clock()
    Play = pygame.image.load('Imagens para MENU/ENTER.png')
    Return = pygame.image.load('Imagens para MENU/Return.png')

    # Pausando Jogo
    def pause():
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False

    while pause:
        nave.movimento()
        clock.tick(80)
        tela.blit(background, (0, 0))

        Texto_Perdeu = Fonte_Texto2.render('Game Over', True, (204, 50, 50))
        Texto_Coin = Fonte_Texto1.render(f'Coin: {coin}', True, (255, 255, 255))
        Texto_MaxCoin = Fonte_Texto1.render(f'MaxCoin: {maxcoin}', True, (255, 255, 255))
        Texto_Score = Fonte_Texto1.render(f'Score: {score}', True, (255, 255, 255))
        Texto_HighScore = Fonte_Texto1.render(f'HighScore: {highscore}', True, (255, 255, 255))
        Texto_Coin_2 = Fonte_Texto1.render(f'Coin: {coin}', True, (255, 255, 0))
        Texto_MaxCoin_2 = Fonte_Texto1.render(f'Coins Max: {maxcoin}', True, (255, 255, 0))       
                                              
                                              
        def textos():
            tela.blit(Texto_Coin, (570, 0))
            tela.blit(Texto_MaxCoin, (820, 0))
            tela.blit(Texto_Score, (0, 0))
            tela.blit(Texto_HighScore, (200, 0))
        textos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause()
                elif event.key == K_BACKSPACE:
                    #pygame.mixer.music.load('Músicas/Snes.mp3')
                    #pygame.mixer.pause()
                    menu()
                elif event.key == K_q:
                    pygame.quit()
                    quit()

        # Condições para Pipes
        if is_off_screen(pipe_group.sprites()[0]):  # se estiver fora da tela
            pipe_group.remove(pipe_group.sprites()[0])  # vai remover os canos fora da tela
            pipe_group.remove(pipe_group.sprites()[0])

            pipes = get_random_pipes(largura * 1.15)  # vai gerar novos canos
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])

        # Colisoes do Jogo
        colisoes = pygame.sprite.spritecollide(nave, Asteroides_Sprites, False, pygame.sprite.collide_mask)
        colisoes2 = pygame.sprite.spritecollide(nave, Satellite_Sprites, False, pygame.sprite.collide_mask)
        colisoes3 = pygame.sprite.spritecollide(nave, Planetas_Sprites, False, pygame.sprite.collide_mask)
        colisoes4 = pygame.sprite.spritecollide(nave, Moeda_Sprites, bool(pygame.sprite.collide_rect))
        colisoes5 = pygame.sprite.spritecollide(nave, pipe_group, False, pygame.sprite.collide_mask)

        Nave_Sprites.draw(tela)
        Asteroides_Sprites.draw(tela)
        Moeda_Sprites.draw(tela)
        Satellite_Sprites.draw(tela)
        Planetas_Sprites.draw(tela)
        pipe_group.draw(tela)
                                              
        def menu_morte():
           tela = pygame.display.set_mode((largura, altura))
           pygame.display.set_caption('Rota de Fuga')
           background = pygame.image.load('Imagens/Mapa-2.jpg')
           mural = pygame.image.load('Imagens para MENU/CARD_KILL.png')
           mural = pygame.transform.scale(mural, (500, 300))

           pos = pygame.mouse.get_pos()
           click = pygame.mouse.get_pressed()
           tela.blit(background, (0, 0))
           tela.blit(mural, (230, 50))
           tela.blit(Texto_Perdeu, (340, 75))
           tela.blit(Texto_HighScore, (335, 215))
           tela.blit(Texto_Score, (350, 180))
           tela.blit(Texto_Coin_2, (350, 290))
           tela.blit(Texto_MaxCoin_2, (335, 255))
           tela.blit(Play, (380, 362))
           tela.blit(Return, (0, 362))
           if 380 <= pos[0] <= 565 and 362 <= pos[1] <= 408:
               if click[0] == 1:
                   game()
           elif 0 <= pos[0] <= 185 and 362 <= pos[1] <= 408:
               if click[0] == 1:
                   menu()

        if colisoes or colisoes2 or colisoes3 or colisoes5:
            #pygame.mixer.music.load('Músicas/Snes.mp3')
            #pygame.mixer.music.stop()
            #sprites.append(pygame.image.load('Naves/Bomba.png'))
            menu_morte()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    game()
                if event.key == K_BACKSPACE:
                    menu()
                                              
        else:
            if score <= 2000:
                Asteroides_Sprites.update()
            if score >= 2000:
                Asteroides_Sprites.remove(Asteroides_Sprites)
                Satellite_Sprites.update()
            if score >= 4000:
                Satellite_Sprites.remove(Satellite_Sprites)
                Planetas_Sprites.update()
            if score >= 5000:
                Planetas_Sprites.remove(Planetas_Sprites)
                pipe_group.update()

            Nave_Sprites.update()
            Moeda_Sprites.update()
            score += 1

        if colisoes4:
            #Coin.play()
            coin = coin + 1
            Moeda_Sprites.add(Moeda())

        # Pontuação
        tela.blit(Texto_Coin, (570, 0))
        tela.blit(Texto_MaxCoin, (750, 0))
        tela.blit(Texto_Score, (0, 0))
        tela.blit(Texto_HighScore, (200, 0))

        # Arquivo Moeda
        file = open('maxcoin.txt', 'r')
        maxcoin = file.read()

        if coin > int(maxcoin):
            maxcoin = coin

        file = open('maxcoin.txt', 'w')
        file.write(f'{maxcoin}')
        file.close()

        # Arquivo Pontuação
        file = open('highscore.txt', 'r')
        highscore = file.read()

        if score > int(highscore):
            highscore = score

        file = open('highscore.txt', 'w')
        file.write(f'{highscore}')
        file.close()

        pygame.display.update()

def menu():
    tela = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Rota de Fuga')

    font = pygame_menu.font.FONT_8BIT
    mybackground = pygame_menu.baseimage.BaseImage(image_path='Menu/Mapa-2.jpg',
                                                   drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    mytheme = pygame_menu.themes.THEME_DARK.copy()
    mytheme.widget_font = font
    mytheme.background_color = mybackground
    mytheme.title_font_shadow = True
    mytheme.widget_padding = 8
    mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE

    menu = pygame_menu.Menu(title='Rota de Fuga', width=1000, height=400, theme=mytheme)
    menu.add.button('Historia', historia)
    menu.add.button('Iniciar', game)
    menu.add.button('Loja', loja)
    menu.add.button('Controles', controles)
    menu.add.button('Creditos', creditos)
    menu.add.button('GitHub', github)
    menu.add.button('Sair', pygame_menu.events.EXIT)
    menu.add.clock(font_size=25, font_name=pygame_menu.font.FONT_DIGITAL)
    menu.mainloop(tela)

menu()

      
