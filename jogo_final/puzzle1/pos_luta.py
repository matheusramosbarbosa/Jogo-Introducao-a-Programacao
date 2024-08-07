import pygame
from objetos_personagem import Infos_Coletaveis
from objetos_personagem import infos_coletaveis

def comecar_pos_luta():
    pygame.init()
    tela = pygame.display.set_mode((1280, 720))
    todos_sprites = pygame.sprite.Group()
    relogio = pygame.time.Clock()
    tempo = relogio.tick()
    pygame.mixer.music.load('puzzle1/sons-batalha/toby fox - UNDERTALE Soundtrack - 31 Waterfall.mp3')
    pygame.mixer.music.play(-1)

    class Cenario(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/boss-area-cac.png')
            self.rect = self.image.get_rect(center=(640, 360))

    cenario = Cenario(todos_sprites)

    # Exibe as informações dos coletáveis:
    def visualizar_infos_coletaveis():
        view_infos_coletaveis = pygame.image.load('puzzle1/visualizacao_coletaveis.png')
        tela.blit(view_infos_coletaveis, (10, 220))

        fonte = pygame.font.SysFont('freesansbold.ttf', 70)

        txt_info_cracha = fonte.render(str(infos_coletaveis.qtd_cracha), True, (255, 255, 255))
        tela.blit(txt_info_cracha, (80, 235))

        txt_info_fragmento_2 = fonte.render(str(infos_coletaveis.qtd_fragmento_2), True, (255, 255, 255))
        tela.blit(txt_info_fragmento_2, (80, 312))

        txt_info_fragmento_1 = fonte.render(str(infos_coletaveis.qtd_fragmento_1), True, (255, 255, 255))
        tela.blit(txt_info_fragmento_1, (80, 388))

        pygame.display.flip()
    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()

    class Personagem:
        # Define a função de incialização do objeto Personagem:
        def __init__(self, x, y):
            self.x = y - 200
            self.y = y + 80
            self.direcao = 'esquerda'
            self.passo = 0
            self.contador_passos = 0
            self.movimento = False

        # Função para desenhar o personagem:
        def desenhar(self, tela, moveu, x, y, passo):
            if passo > 0 and passo % 2 == 0:
                passo = 0
            else:
                passo = 1
            self.imagens = [pygame.image.load('puzzle1/imagens-batalha/prota-esquerda-1.png'), pygame.image.load(
                'puzzle1/imagens-batalha/prota-esquerda-2.png')]
            self.imagens_parado = pygame.image.load('puzzle1/imagens-batalha/prota-esquerda-0.png')
            if moveu:
                tela.blit(self.imagens[passo], (x, y))
            else:
                tela.blit(self.imagens_parado, (x, y))

    x = 420
    y = 330
    passos = 0
    Personagem.desenhar(Personagem, tela, False, x, y, passos)
    visualizar_infos_coletaveis()
    pygame.display.update()
    for i in range(3):
        class Boss(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load(f'puzzle1/imagens-batalha/boss-morre-{i}.png')
                self.rect = self.image.get_rect(center=(240, 340))

        boss = Boss(todos_sprites)
        visualizar_infos_coletaveis()
        todos_sprites.update(tempo)
        todos_sprites.draw(tela)
        Personagem.desenhar(Personagem, tela, False, x, y, passos)
        visualizar_infos_coletaveis()
        pygame.display.update()
        pygame.time.wait(350)
        boss.remove(todos_sprites)

    class Cracha(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/cracha-drop.png')
            self.rect = self.image.get_rect(center=(240, 390))

    cracha = Cracha(todos_sprites)
    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    cracha_dropado = True
    moveu = False

    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    Personagem.desenhar(Personagem, tela, False, x, y, passos)
    visualizar_infos_coletaveis()
    pygame.display.update()
    while cracha_dropado:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x -= 20
                    passos += 1
                    if x < 235:
                        cracha_dropado = False
                        cracha.remove(todos_sprites)
                        item = pygame.mixer.Sound('puzzle1/sons-batalha/item get 1.wav')
                        item.play()
                        infos_coletaveis.qtd_cracha += 1
                        visualizar_infos_coletaveis()
                        todos_sprites.update(tempo)
                        todos_sprites.draw(tela)
                        Personagem.desenhar(Personagem, tela, True, x, y, passos)
                        visualizar_infos_coletaveis()
                        pygame.display.update()
                        pygame.time.wait(1000)
                    else:
                        visualizar_infos_coletaveis()
                        todos_sprites.update(tempo)
                        todos_sprites.draw(tela)
                        Personagem.desenhar(Personagem, tela, True, x, y, passos)
                        visualizar_infos_coletaveis()
                        pygame.display.update()