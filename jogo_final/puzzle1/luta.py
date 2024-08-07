import pygame
from pos_luta import comecar_pos_luta
from objetos_personagem import Infos_Coletaveis
from objetos_personagem import infos_coletaveis

def comecar_luta():
    tentar = True
    pygame.init()
    tentativas = 0
    while tentar:
        tela = pygame.display.set_mode((1280, 720))
        relogio = pygame.time.Clock()
        todos_sprites = pygame.sprite.Group()
        pb = pygame.sprite.Group()
        pd = pygame.sprite.Group()
        hp_jogador_inicial = 200
        hp_jogador = hp_jogador_inicial
        ataque_jogador = 40
        if tentativas <= 1:
            for i in range(3):
                class Tutorial(pygame.sprite.Sprite):
                    def __init__(self, groups):
                        super().__init__(groups)
                        self.image = pygame.image.load(f'puzzle1/imagens-batalha/explica{i}.png')
                        self.rect = self.image.get_rect(center=(640, 502))
                tutorial = Tutorial(todos_sprites)
                tela.fill('black')

                # Exibe as informações dos coletáveis:
                def visualizar_infos_coletaveis():
                    view_infos_coletaveis = pygame.image.load('puzzle1/visualizacao_coletaveis.png')
                    tela.blit(view_infos_coletaveis, (10, 220))

                    fonte = pygame.font.SysFont('puzzle1/freesanbold.ttf', 70)

                    txt_info_cracha = fonte.render(str(infos_coletaveis.qtd_cracha), True, (255, 255, 255))
                    tela.blit(txt_info_cracha, (80, 235))

                    txt_info_fragmento_2 = fonte.render(str(infos_coletaveis.qtd_fragmento_2), True, (255, 255, 255))
                    tela.blit(txt_info_fragmento_2, (80, 312))

                    txt_info_fragmento_1 = fonte.render(str(infos_coletaveis.qtd_fragmento_1), True, (255, 255, 255))
                    tela.blit(txt_info_fragmento_1, (80, 388))

                    pygame.display.flip()

                visualizar_infos_coletaveis()
                todos_sprites.update(relogio)
                todos_sprites.draw(tela)
                visualizar_infos_coletaveis()
                pygame.display.update()
                tutorial.remove(todos_sprites)
                pygame.time.wait(2500)
                if i == 1:
                    pygame.time.wait(2500)

        # boss 272 332 374
        class Boss(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load('puzzle1/imagens-batalha/boss-luta.png').convert_alpha()
                self.rect = self.image.get_rect(center=(660, 200))
        class Barra_boss(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load('puzzle1/imagens-batalha/BOSS.png').convert_alpha()
                self.rect = self.image.get_rect(center=(420, 410))
        barra_boss = Barra_boss(todos_sprites)
        class Barra_jogador(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load('puzzle1/imagens-batalha/VIDA.png').convert_alpha()
                self.rect = self.image.get_rect(center=(515, 690))
        barra_jogador = Barra_jogador(todos_sprites)
        boss = Boss(todos_sprites)
        boss2 = Boss(pb)
        boss3 = Boss(pd)


        # indica 14 128
        class Barra(pygame.sprite.Sprite):
            def __init__(self, groups):
                super().__init__(groups)
                self.image = pygame.image.load('puzzle1/imagens-batalha/ataque barra.png').convert_alpha()
                self.rect = self.image.get_rect(center=(640, 502))


        barra = Barra(todos_sprites)

        # barra 578 148 (14 direita
        hp_boss_inicial = 400
        hp_boss = hp_boss_inicial
        ataque_boss = 100
        pygame.mixer.music.load("puzzle1/sons-batalha/ELDEN RING - Lichdragon Fortissax Chiptune_8-bit Cover.mp3")
        pygame.mixer.music.play(-1)
        ataque_som = pygame.mixer.Sound('puzzle1/sons-batalha/undertale-sound-effect-attack-made-with-Voicemod.mp3')
        luta = True
        derrota = False
        vitoria = False
        tempo = relogio.tick()
        visualizar_infos_coletaveis()
        todos_sprites.update(tempo)
        todos_sprites.draw(tela)
        visualizar_infos_coletaveis()
        pygame.display.update()
        while luta:

            visualizar_infos_coletaveis()
            todos_sprites.update(tempo)
            tela.fill('black')
            todos_sprites.draw(tela)
            visualizar_infos_coletaveis()
            pygame.display.update()
            batalha = True
            x = 351
            barra_ataque = pygame.Vector2(0, 360)
            ataque = False


            class prebatalha(pygame.sprite.Sprite):
                def __init__(self, groups):
                    super().__init__(groups)
                    self.image = pygame.image.load('puzzle1/imagens-batalha/prebatalha.png').convert_alpha()
                    self.rect = self.image.get_rect(center=(640, 502))


            prebat = prebatalha(pb)
            visualizar_infos_coletaveis()
            pb.update(tempo)
            tela.fill('black')
            pb.draw(tela)
            visualizar_infos_coletaveis()
            pygame.display.update()
            pygame.time.wait(1500)
            retangulo1 = pygame.Rect(440, 400, hp_boss, 20)
            retangulo3 = pygame.Rect(540, 680, hp_jogador, 20)
            pygame.draw.rect(tela, (255, 249, 174), retangulo1)
            pygame.draw.rect(tela, (255, 249, 174), retangulo3)
            while not ataque:
                class Indicador(pygame.sprite.Sprite):
                    def __init__(self, groups):
                        super().__init__(groups)
                        self.image = pygame.image.load('puzzle1/imagens-batalha/ataque indicador.png').convert_alpha()
                        self.rect = self.image.get_rect(center=(x, 502))

                indicador = Indicador(todos_sprites)
                visualizar_infos_coletaveis()
                todos_sprites.update(tempo)
                todos_sprites.draw(tela)
                visualizar_infos_coletaveis()
                pygame.display.update()
                retangulo1 = pygame.Rect(440, 400, hp_boss, 20)
                retangulo3 = pygame.Rect(540, 680, hp_jogador, 20)
                pygame.draw.rect(tela, (255, 249, 174), retangulo1)
                pygame.draw.rect(tela, (255, 249, 174), retangulo3)
                diferenca1 = hp_boss_inicial - hp_boss
                diferenca2 = hp_jogador_inicial - hp_jogador
                if diferenca1 > 0:
                    pygame.draw.rect(tela, 'red', retangulo2)
                if diferenca2 > 0:
                    pygame.draw.rect(tela, 'red', retangulo4)
                visualizar_infos_coletaveis()
                pygame.display.update()
                eventos1 = pygame.event.get()
                for event in eventos1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            ataque = True
                            porcentagem1 = (100 - (abs(x - 640) / 289) * 100) / 100
                            dano = int(ataque_jogador * porcentagem1)
                            hp_boss -= dano
                            diferenca1 = hp_boss_inicial - hp_boss
                            retangulo1 = pygame.Rect(440, 400, hp_boss, 20)
                            pygame.draw.rect(tela, (255, 249, 174), retangulo1)
                            if diferenca1 > 0:
                                ret_x2 = 440 + hp_boss
                                retangulo2 = pygame.Rect(ret_x2, 400, diferenca1, 20)
                                pygame.draw.rect(tela, 'red', retangulo2)
                            visualizar_infos_coletaveis()
                            pygame.display.update()
                            ataque_som.play(0)
                            for  j in range(3):
                                class Ataques(pygame.sprite.Sprite):
                                    def __init__(self, groups):
                                        super().__init__(groups)
                                        self.image = pygame.image.load(f'puzzle1/imagens-batalha/ATAQUE{j+1}.png').convert_alpha()
                                        self.rect = self.image.get_rect(center=(600, 200))
                                ataque = Ataques(todos_sprites)
                                visualizar_infos_coletaveis()
                                todos_sprites.update(tempo)
                                todos_sprites.draw(tela)
                                visualizar_infos_coletaveis()
                                pygame.display.update()
                                pygame.time.wait(64)
                                ataque.remove(todos_sprites)


                if not ataque:
                    if x <= 929:
                        if hp_boss < 300:
                            if hp_boss < 100:
                                x += 4.3
                                ataque_boss = 150
                            elif hp_boss < 200:
                                x += 4
                                ataque_boss = 120
                            else:
                                x += 3.7
                                ataque_boss = 110
                        else:
                            x += 3.4
                    else:
                        ataque = True
                indicador.remove(todos_sprites)
            pygame.time.wait(500)
            if hp_boss > 0:

                x = 351

                defesa = False


                class predefesa(pygame.sprite.Sprite):
                    def __init__(self, groups):
                        super().__init__(groups)
                        self.image = pygame.image.load('puzzle1/imagens-batalha/predefesa.png').convert_alpha()
                        self.rect = self.image.get_rect(center=(640, 502))


                predef = predefesa(pd)
                visualizar_infos_coletaveis()
                pd.update(tempo)
                tela.fill('black')
                pd.draw(tela)
                visualizar_infos_coletaveis()
                pygame.display.update()
                pygame.time.wait(1500)
                while not defesa:

                    class Indicador(pygame.sprite.Sprite):
                        def __init__(self, groups):
                            super().__init__(groups)
                            self.image = pygame.image.load('puzzle1/imagens-batalha/ataque indicador.png').convert_alpha()
                            self.rect = self.image.get_rect(center=(x, 502))


                    indicador = Indicador(todos_sprites)
                    visualizar_infos_coletaveis()
                    todos_sprites.update(tempo)
                    todos_sprites.draw(tela)
                    retangulo1 = pygame.Rect(440, 400, hp_boss, 20)
                    retangulo3 = pygame.Rect(540, 680, hp_jogador, 20)
                    pygame.draw.rect(tela, (255, 249, 174), retangulo1)
                    pygame.draw.rect(tela, (255, 249, 174), retangulo3)
                    diferenca1 = hp_boss_inicial - hp_boss
                    diferenca2 = hp_jogador_inicial - hp_jogador
                    if diferenca1 > 0:
                        pygame.draw.rect(tela, 'red', retangulo2)
                    if diferenca2 > 0:
                        pygame.draw.rect(tela, 'red', retangulo4)
                    visualizar_infos_coletaveis()
                    pygame.display.update()
                    eventos2 = pygame.event.get()
                    for event in eventos2:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                defesa = True
                                porcentagem2 = (abs(x - 640) / 289)
                                dano2 = int(ataque_boss * porcentagem2)
                                hp_jogador -= dano2
                                diferenca2 = hp_jogador_inicial - hp_jogador
                                retangulo3 = pygame.Rect(540, 680, hp_jogador, 20)
                                pygame.draw.rect(tela, (255, 249, 174), retangulo3)
                                if diferenca2 > 0:
                                    ret_x3 = 540 + hp_jogador
                                    retangulo4 = pygame.Rect(ret_x3, 680, diferenca2, 20)
                                    pygame.draw.rect(tela, 'red', retangulo4)
                                visualizar_infos_coletaveis()
                                pygame.display.update()

                    if not defesa:
                        if x <= 929:
                            if hp_boss < 300:
                                if hp_boss < 100:
                                    x += 2.2
                                    ataque_boss = 150
                                elif hp_boss < 200:
                                    x += 1.8
                                    ataque_boss = 120
                                else:
                                    x += 1.5
                                    ataque_boss = 110
                            else:
                                x += 1.2

                        else:
                            defesa = True
                            dano2 = ataque_boss
                            hp_jogador -= dano2
                            diferenca2 = hp_jogador_inicial - hp_jogador
                            retangulo3 = pygame.Rect(540, 680, hp_jogador, 20)
                            pygame.draw.rect(tela, (255, 249, 174), retangulo3)
                            if diferenca2 > 0:
                                ret_x3 = 540 + hp_jogador
                                retangulo4 = pygame.Rect(ret_x3, 680, diferenca2, 20)
                                pygame.draw.rect(tela, 'red', retangulo4)
                            visualizar_infos_coletaveis()
                            pygame.display.update()
                    indicador.remove(todos_sprites)
                pygame.time.wait(500)
            else:
                tentar = False
                luta = False
            if hp_jogador < 0:
                derrota = True
                luta = False
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load(
                    "puzzle1/sons-batalha/1.16 Toby Fox - DELTARUNE Chapter 2 OST - 16 Faint Courage (Game Over).mp3")
                pygame.mixer.music.play(-1)
                tentativas += 1
                for i in range (5):
                    recomeco = pygame.sprite.Group()
                    class Recomecar(pygame.sprite.Sprite):
                        def __init__(self, groups):
                            super().__init__(groups)
                            self.image = pygame.image.load(f'puzzle1/imagens-batalha/REM{5 - i}.png').convert_alpha()
                            self.rect = self.image.get_rect(center=(640, 360))
                    recomecar = Recomecar(recomeco)
                    tela.fill('black')
                    visualizar_infos_coletaveis()
                    recomeco.update(tempo)
                    recomeco.draw(tela)
                    visualizar_infos_coletaveis()
                    pygame.display.update()
                    pygame.time.wait(1500)
                    recomecar.remove(recomeco)
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()

    comecar_pos_luta()