import pygame
from luta import comecar_luta
from objetos_personagem import Infos_Coletaveis
from objetos_personagem import infos_coletaveis

def comecar_intro_batalha():
    pygame.init()
    tela = pygame.display.set_mode((1280, 720))
    tela.fill(('black'))
    todos_sprites = pygame.sprite.Group()
    tempo = pygame.time.Clock()
    pygame.mixer.music.load("puzzle1/sons-batalha/toby fox - UNDERTALE Soundtrack - 31 Waterfall.mp3")
    pygame.mixer.music.play(-1)
    # Define a classe do personagem, com as características do objeto:
    class Cenario(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/entrada cac.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 360)) #87x86
    cenario = Cenario(todos_sprites)
    class Idoso(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/idoso.png').convert_alpha()
            self.rect = self.image.get_rect(center=(1050, 440)) #87x86
    idoso = Idoso(todos_sprites)
    y = 720
    i = 1
    while y > 440:
        class Personagem(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load(f'puzzle1/imagens-batalha/prota-costas-{i}.png').convert_alpha()
                self.rect = self.image.get_rect(center=(970, y))
        personagem = Personagem(todos_sprites)

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
        pygame.time.wait(200)
        if i == 2:
            i = 0
        i += 1
        y -= 20
        personagem.remove(todos_sprites)

    class Personagem(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/prota-direita-0.png').convert_alpha()
            self.rect = self.image.get_rect(center=(970, y))


    class Dialogo1(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/espere.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    personagem = Personagem(todos_sprites)
    dialogo1 = Dialogo1(todos_sprites)
    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(750)
    dialogo1.remove(todos_sprites)

    class Dialogo2(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/voce-vai-precisar-disso.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo2 = Dialogo2(todos_sprites)

    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    dialogo2.remove(todos_sprites)
    pygame.time.wait(1300)
    class Dialogo3(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/voce-obteve.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))

    item =pygame.mixer.Sound('puzzle1/sons-batalha/item get 1.wav')
    item.play()
    dialogo3 = Dialogo3(todos_sprites)

    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    dialogo3.remove(todos_sprites)
    pygame.time.wait(1700)
    class Dialogo4(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'puzzle1/imagens-batalha/agora.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo4 = Dialogo4(todos_sprites)

    visualizar_infos_coletaveis()
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    dialogo4.remove(todos_sprites)
    pygame.time.wait(750)
    personagem.remove(todos_sprites)
    while y > 140:
        class Personagem(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load(f'puzzle1/imagens-batalha/prota-costas-{i}.png').convert_alpha()
                self.rect = self.image.get_rect(center=(970, y))
        personagem = Personagem(todos_sprites)

        visualizar_infos_coletaveis()
        todos_sprites.update(tempo)
        todos_sprites.draw(tela)
        visualizar_infos_coletaveis()
        pygame.display.update()
        pygame.time.wait(200)
        if i == 2:
            i = 0
        i += 1
        y -= 30
        personagem.remove(todos_sprites)

    tela.fill(('white'))
    infos_coletaveis.qtd_fragmento_1 -= 1
    infos_coletaveis.qtd_fragmento_2 -= 1
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(500)
    todos_sprites2 = pygame.sprite.Group()

    class Cenario2(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/boss-area-cac.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 360))
    cenario2 = Cenario2(todos_sprites2)


    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    class Boss(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/boss-direita.png').convert_alpha()
            self.rect = self.image.get_rect(center=(240, 340))
    boss = Boss(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    y = 800
    while y > 370:
        class Personagem(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load(f'puzzle1/imagens-batalha/prota-costas-{i}.png').convert_alpha()
                self.rect = self.image.get_rect(center=(1000, y))
        personagem = Personagem(todos_sprites2)
        visualizar_infos_coletaveis()
        todos_sprites2.update(tempo)
        todos_sprites2.draw(tela)
        visualizar_infos_coletaveis()
        pygame.display.update()
        pygame.time.wait(200)
        if i == 2:
            i = 0
        i += 1
        y -= 20
        personagem.remove(todos_sprites2)
    x = 1000
    while x > 420:
        class Personagem(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load(f'puzzle1/imagens-batalha/prota-esquerda-{i}.png').convert_alpha()
                self.rect = self.image.get_rect(center=(x, y))
        personagem = Personagem(todos_sprites2)
        visualizar_infos_coletaveis()
        todos_sprites2.update(tempo)
        todos_sprites2.draw(tela)
        visualizar_infos_coletaveis()
        pygame.display.update()
        pygame.time.wait(200)
        if i == 2:
            i = 0
        i += 1
        x -= 25
        personagem.remove(todos_sprites2)
    class Personagem(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/prota-esquerda-0.png').convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))
    personagem = Personagem(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    class Dialogo1(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/entaovcchegou.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo1 = Dialogo1(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(1500)
    dialogo1.remove(todos_sprites2)
    class Dialogo2(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/esperando.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo2 = Dialogo2(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(2000)
    dialogo2.remove(todos_sprites2)
    class Dialogo3(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/ameaça.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo3 = Dialogo3(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(2500)
    dialogo3.remove(todos_sprites2)
    class Dialogo3(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/vou contar.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo3 = Dialogo3(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(2500)
    dialogo3.remove(todos_sprites2)
    class Dialogo3(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/plano.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo3 = Dialogo3(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(3200)
    dialogo3.remove(todos_sprites2)
    class Dialogo3(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/ninguem.png').convert_alpha()
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo3 = Dialogo3(todos_sprites2)
    visualizar_infos_coletaveis()
    todos_sprites2.update(tempo)
    todos_sprites2.draw(tela)
    visualizar_infos_coletaveis()
    pygame.display.update()
    pygame.time.wait(2300)
    dialogo3.remove(todos_sprites2)
    boss.remove(todos_sprites2)
    for j in range(6):
        class Boss(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load(f'puzzle1/imagens-batalha/boss-arma-{j}.png').convert_alpha()
                self.rect = self.image.get_rect(center=(240, 340))
        boss = Boss(todos_sprites2)
        visualizar_infos_coletaveis()
        todos_sprites2.update(tempo)
        todos_sprites2.draw(tela)
        visualizar_infos_coletaveis()
        pygame.display.update()
        pygame.time.wait(150)
        boss.remove(todos_sprites2)

    comecar_luta()