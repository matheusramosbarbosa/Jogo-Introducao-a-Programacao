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