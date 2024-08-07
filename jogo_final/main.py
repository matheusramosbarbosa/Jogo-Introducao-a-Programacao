# from configuracoes import *
# from pytmx.util_pygame import load_pygame
# from os.path import join # Importa a função join do módulo os.path

# from sprites import Sprite, PlantinhasSprite, AnimatedSprite, BorderSprite, CollidableSprite, SpriteTransicao
# from entities import Player, Character
# from grupos import TodosSprites

# from support import *

# class Game:
# # geral
#     def __init__(self):
#         self.teve_colisao = False  # Flag para controlar se a opacidade já foi alterada
#         pygame.init()
#         self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#         pygame.display.set_caption('Em Busca do Crachá Perdido')
#         self.clock = pygame.time.Clock()

#         # grupos
#         self.todos_sprites = TodosSprites()
#         self.sprites_colisoes = pygame.sprite.Group()
#         self.sprites_transicao = pygame.sprite.Group()

#         # transicao
#         self.transition_target = None
#         self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
#         self.tint_mode = 'untint'
#         self.tint_progress = 0
#         self.tint_direction = -1
#         self.tint_speed = 600

#         self.import_assets()
#         self.setup(self.mapas['mundo'], 'inicio')

# # sistema de interação
#     def input(self):
#         tecla = pygame.key.get_just_pressed()
#         if tecla[pygame.K_SPACE]:
#             for obj in self.mapas['mundo'].get_layer_by_name('portasobj'):
#                 if self.player.rect.colliderect(pygame.Rect(obj.x, obj.y, obj.width, obj.height)):
#                 # if self.player.rect.colliderect(pygame.Rect(obj.x, obj.y, obj.width, obj.height)):
#                     print('colidiu')

#     def import_assets(self):
#         self.mapas = {'mundo': load_pygame(join('data', 'mapas', 'mapainfinito.tmx')), 
#                       'ccen': load_pygame(join('data', 'mapas', 'ccen.tmx')),
#                       'voxarlabs': load_pygame(join('data', 'mapas', 'voxarlabs.tmx'))}
#         self.frames_do_mundo = {
#             'personagens': all_character_import('graficos', 'personagem')
#         }

#     def setup(self, mapa, player_start_pos):
#         # limpar o mapa
#         for group in (self.todos_sprites, self.sprites_colisoes, self.sprites_transicao):
#             group.empty()
        
#         for camada in ['interno', 'terreno', 'furniture', 'upper', 'detalhes', 'carros', 'parede']:
#         # terreno // ordem importa
#             for x, y, surf in mapa.get_layer_by_name(camada).tiles():
#                 Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['fundo'])
                

#         for camada in ['portas']:
#         # terreno // ordem importa
#             for x, y, surf in mapa.get_layer_by_name(camada).tiles():
#                 Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['fundo'])

#         for camada in ['pilares']:
#         # terreno // ordem importa
#             for x, y, surf in mapa.get_layer_by_name(camada).tiles():
#                 Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['cima'])
                
#         for camada in ['teto', 'teto1andar',  'detalhesparede', '1andar','barreira do mapa']:
#         # terreno // ordem importa
#             for x, y, surf in mapa.get_layer_by_name(camada).tiles():
#                 Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['cima'])

#         # objetos
#         for obj in mapa.get_layer_by_name('Objetos'):
#             if obj.name == 'top':
#                 Sprite((obj.x, obj.y), obj.image, self.todos_sprites, WORLD_LAYERS['cima'])
#             else:
#                 CollidableSprite((obj.x, obj.y), obj.image, (self.todos_sprites, self.sprites_colisoes))

#         # objetos de transicao
#         for obj in self.mapas['mundo'].get_layer_by_name('portasobj'):
#             SpriteTransicao((obj.x, obj.y), (obj.width, obj.height), (obj.properties['target'], obj.properties['pos']), self.sprites_transicao)
        
#         for obj in self.mapas['ccen'].get_layer_by_name('portasobj'):
#             SpriteTransicao((obj.x, obj.y), (obj.width, obj.height), (obj.properties['target'], obj.properties['pos']), self.sprites_transicao)

#         # colisoes
#         for obj in mapa.get_layer_by_name('Collisions'):
#             BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.sprites_colisoes)

#         # plantinhas
#         for obj in mapa.get_layer_by_name('plantinhas'):
#             PlantinhasSprite((obj.x, obj.y), obj.image, self.todos_sprites)

#         # entidades
#         for obj in mapa.get_layer_by_name('Entities'):
#             if obj.name == 'Player':
#                 if obj.properties['pos'] == player_start_pos:
#                     self.player = Player(
#                         pos = (obj.x, obj.y),
#                         frames = self.frames_do_mundo['personagens']['protagonista2'],
#                         groups = self.todos_sprites, sprites_colisoes = self.sprites_colisoes)
#             else:
#                 Character(
#                     pos = (obj.x, obj.y),
#                     frames = self.frames_do_mundo['personagens'][obj.properties['graphic']],
#                     groups = self.todos_sprites)

#     def checar_transicao(self):
#         sprites = [sprite for sprite in self.sprites_transicao if sprite.rect.colliderect(self.player.hitbox)]
#         if sprites:
#             self.player.block()
#             self.transition_target = sprites[0].target
#             self.tint_mode = 'tint'

#     def check_collision(self):
#         # Acessa a camada de objetos 'opacidade'
#         opacidade_layer = self.mapas['mundo'].get_layer_by_name('opacidade')
        
#         player_collided = False
#         for obj in opacidade_layer:
#             # Criar um retângulo para o objeto
#             obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            
#             # Verificar colisão com o jogador
#             if self.player.rect.colliderect(obj_rect):
#                 player_collided = True
#                 break

#         # Se houve colisão e ainda não alterou a opacidade, altere
#         if player_collided and not self.teve_colisao:
#             self.alterar_opacidade_tetos(100)  # Define a opacidade como 100
#             self.teve_colisao = True  # Marca que a opacidade foi alterada
#         # Se não houve colisão e a opacidade estava alterada, restaura
#         elif not player_collided and self.teve_colisao:
#             self.alterar_opacidade_tetos(255)  # Restaura a opacidade original
#             self.teve_colisao = False  # Reseta a flag

#     def alterar_opacidade_tetos(self, opacidade):
#         camadas_teto = ['teto', 'teto1andar', 'detalhesparede', '1andar', 'barreira do mapa']
        
#         for camada_nome in camadas_teto:
#             camada = self.mapas['mundo'].get_layer_by_name(camada_nome)
            
#             # Apenas ajustar opacidade se os tiles estiverem próximos ao jogador
#             for x, y, surf in camada.tiles():
#                 # Verifica se o tile está próximo do jogador
#                 if abs(self.player.rect.centerx - x * TILE_SIZE) < 100 and \
#                 abs(self.player.rect.centery - y * TILE_SIZE) < 100:
#                     surf.set_alpha(opacidade)  # Define a opacidade da superfície do tile


#     def tint_screen(self, dt):
#         if self.tint_mode == 'untint':
#             self.tint_progress -= self.tint_speed * dt

#         if self.tint_mode == 'tint':
#             self.tint_progress += self.tint_speed * dt
#             if self.tint_progress >= 255:
#                 self.setup(self.mapas[self.transition_target[0]], self.transition_target[1])
#                 self.tint_mode = 'untint'
#                 self.transition_target = None

#         self.tint_progress = max(0, min(self.tint_progress, 255))
#         self.tint_surf.set_alpha(self.tint_progress) # Define a transparência da superfície de cor
#         self.display_surface.blit(self.tint_surf, (0,0))


#     def run(self):
#         while True:
#             dt = self.clock.tick() / 1000
#             self.display_surface.fill('black')

#             # event loop
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()

#             # game logic
#             self.input()
#             self.checar_transicao()
#             self.check_collision()
#             self.todos_sprites.update(dt)

#             # desenhando
#             self.todos_sprites.draw(self.player.rect.center)

#             self.tint_screen(dt)

#             # atualizando a tela
#             pygame.display.update()

# if __name__ == '__main__':
#     game = Game()
#     game.run()

import pygame
from os.path import join  # Importa a função join do módulo os.path para manipular caminhos
from pytmx.util_pygame import load_pygame  # Carrega mapas no formato Tiled
from PIL import Image
import os

# Importações de módulos internos
from configuracoes import *
from sprites import Sprite, PlantinhasSprite, AnimatedSprite, BorderSprite, CollidableSprite, SpriteTransicao
from entities import Player, Character
from grupos import TodosSprites
from support import *

class Jogo:
    # Inicializa as configurações básicas do jogo
    def __init__(self):
        self.houve_colisao = False
        pygame.init()
        self.janela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Em Busca do Crachá Perdido')
        self.relogio = pygame.time.Clock()

        self.gif_frames = self.carregar_gif('graficos/roubocracha/roubo.gif')
        self.mostrar_gif(self.gif_frames)

        self.todos_sprites = TodosSprites()
        self.sprites_colisoes = pygame.sprite.Group()
        self.sprites_transicao = pygame.sprite.Group()

        self.alvo_transicao = None
        self.superficie_tint = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.modo_tint = 'untint'
        self.progresso_tint = 0
        self.direcao_tint = -1
        self.velocidade_tint = 600

        self.importar_recursos()
        self.configurar_jogo(self.mapas['mundo'], 'inicio')

    def carregar_gif(self, caminho):
        gif = Image.open(caminho)
        frames = []
        tamanho_desejado = (1280, 720) 

        try:
            while True:
                frame = gif.copy()
                # Converte o frame do PIL para uma superfície do pygame
                surface = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
                # Redimensiona a superfície
                surface_redimensionada = pygame.transform.scale(surface, tamanho_desejado)
                frames.append(surface_redimensionada)
                gif.seek(len(frames))  # Move para o próximo frame
        except EOFError:
            pass  # Sai quando chegar ao fim do GIF
        return frames
    
    def mostrar_gif(self, frames):
        for frame in frames:
            self.janela.fill((0, 0, 0))
            self.janela.blit(frame, (0, 0))
            pygame.display.update()
            pygame.time.delay(100)
    
    def entrada(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            for obj in self.mapas['voxarlabs'].get_layer_by_name('Objetos'):
                if self.jogador.rect.colliderect(pygame.Rect(obj.x, obj.y, obj.width, obj.height)):
                    if 'interacao' in obj.properties and obj.properties['interacao'] == 'pc1':
                        print('Interação com PC1')
                        self.carregar_e_executar_novo_jogo()

    def carregar_e_executar_novo_jogo(self):
        pygame.quit()  # Fecha o jogo atual
        os.system('python puzzle1/puzzle1_introducao.py')  # Executa o novo jogo
        exit()  # Sai do jogo atual

    # Função para importar os recursos (mapas e gráficos)
    def importar_recursos(self):
        self.mapas = {
            'mundo': load_pygame(join('data', 'mapas', 'mapainfinito.tmx')), 
            'ccen': load_pygame(join('data', 'mapas', 'ccen.tmx')),
            'voxarlabs': load_pygame(join('data', 'mapas', 'voxarlabs.tmx'))
        }
        self.frames_do_mundo = {
            'personagens': all_character_import('graficos', 'personagem')
        }

    # Função para configurar o jogo com base no mapa atual
    def configurar_jogo(self, mapa, posicao_inicial_jogador):
        # Limpa os grupos de sprites
        for grupo in (self.todos_sprites, self.sprites_colisoes, self.sprites_transicao):
            grupo.empty()

        # Configura as camadas de terreno e objetos
        camadas_terreno = ['interno', 'terreno', 'furniture', 'upper', 'detalhes', 'carros', 'parede']
        for camada in camadas_terreno:
            for x, y, surf in mapa.get_layer_by_name(camada).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['fundo'])

        for camada in ['portas']:
            for x, y, surf in mapa.get_layer_by_name(camada).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['fundo'])

        for camada in ['pilares']:
            for x, y, surf in mapa.get_layer_by_name(camada).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['cima'])

        camadas_cima = ['teto', 'teto1andar', 'detalhesparede', '1andar', 'barreira do mapa']
        for camada in camadas_cima:
            for x, y, surf in mapa.get_layer_by_name(camada).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.todos_sprites, WORLD_LAYERS['cima'])


        # Configura os objetos e colisões no mapa
        for obj in mapa.get_layer_by_name('Objetos'):
            if obj.name == 'top':
                Sprite((obj.x, obj.y), obj.image, self.todos_sprites, WORLD_LAYERS['cima'])
            else:
                CollidableSprite((obj.x, obj.y), obj.image, (self.todos_sprites, self.sprites_colisoes))

        # Configura os objetos de transição
        for mapa_nome, mapa_atual in self.mapas.items():
            for obj in mapa_atual.get_layer_by_name('portasobj'):
                SpriteTransicao((obj.x, obj.y), (obj.width, obj.height), 
                                (obj.properties['target'], obj.properties['pos']), self.sprites_transicao)

        # Configura as colisões no mapa
        for obj in mapa.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.sprites_colisoes)

        # Configura as plantinhas no mapa
        for obj in mapa.get_layer_by_name('plantinhas'):
            PlantinhasSprite((obj.x, obj.y), obj.image, self.todos_sprites)

        # Configura as entidades (jogador e NPCs)
        for obj in mapa.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == posicao_inicial_jogador:
                    self.jogador = Player(
                        pos=(obj.x, obj.y),
                        frames=self.frames_do_mundo['personagens']['protagonista2'],
                        groups=self.todos_sprites, sprites_colisoes=self.sprites_colisoes)
            else:
                Character(
                    pos=(obj.x, obj.y),
                    frames=self.frames_do_mundo['personagens'][obj.properties['graphic']],
                    groups=self.todos_sprites)

    # Verifica se o jogador deve iniciar uma transição de mapa
    def verificar_transicao(self):
        sprites_colididos = [sprite for sprite in self.sprites_transicao if sprite.rect.colliderect(self.jogador.hitbox)]
        if sprites_colididos:
            self.jogador.bloquear_movimento()
            self.alvo_transicao = sprites_colididos[0].target
            self.modo_tint = 'tint'

    # Verifica colisões específicas com objetos no mapa
    def checar_colisao(self):
        camada_opacidade = self.mapas['mundo'].get_layer_by_name('opacidade')
        
        jogador_colidiu = False
        for obj in camada_opacidade:
            retangulo_obj = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            
            if self.jogador.rect.colliderect(retangulo_obj):
                jogador_colidiu = True
                break

        if jogador_colidiu and not self.houve_colisao:
            self.alterar_opacidade_tetos(100)
            self.houve_colisao = True
        elif not jogador_colidiu and self.houve_colisao:
            self.alterar_opacidade_tetos(255)
            self.houve_colisao = False

    # Função para alterar a opacidade das camadas do teto quando o jogador colide
    def alterar_opacidade_tetos(self, opacidade):
        camadas_teto = ['teto', 'teto1andar', 'detalhesparede', '1andar', 'barreira do mapa']
        
        for nome_camada in camadas_teto:
            camada = self.mapas['mundo'].get_layer_by_name(nome_camada)
            
            for x, y, surf in camada.tiles():
                if abs(self.jogador.rect.centerx - x * TILE_SIZE) < 100 and \
                   abs(self.jogador.rect.centery - y * TILE_SIZE) < 100:
                    surf.set_alpha(opacidade)

    # Função para gerenciar o efeito de transição de tela
    def tintar_tela(self, dt):
        if self.modo_tint == 'untint':
            self.progresso_tint -= self.velocidade_tint * dt

        if self.modo_tint == 'tint':
            self.progresso_tint += self.velocidade_tint * dt
            if self.progresso_tint >= 255:
                self.configurar_jogo(self.mapas[self.alvo_transicao[0]], self.alvo_transicao[1])
                self.modo_tint = 'untint'
                self.alvo_transicao = None

        self.progresso_tint = max(0, min(self.progresso_tint, 255))
        self.superficie_tint.set_alpha(self.progresso_tint)
        self.janela.blit(self.superficie_tint, (0, 0))

    # Função principal do jogo, que mantém o loop principal rodando
    def rodar(self):
        while True:
            dt = self.relogio.tick() / 1000
            self.janela.fill('black')

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.entrada()
            self.verificar_transicao()
            self.checar_colisao()
            self.todos_sprites.update(dt)

            self.todos_sprites.draw(self.jogador.rect.center)
            self.tintar_tela(dt)

            pygame.display.update()

if __name__ == '__main__':
    jogo = Jogo()
    jogo.rodar()