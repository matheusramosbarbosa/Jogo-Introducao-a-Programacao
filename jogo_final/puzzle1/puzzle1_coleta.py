import pygame
import sys
from objetos_personagem import Personagem_1d
from puzzle2_introducao import comecar_puzzle2
from objetos_personagem import Infos_Coletaveis
from objetos_personagem import infos_coletaveis

status_coleta = False

# Define a classe do Jogo:
class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1280
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')
        icone = pygame.image.load('puzzle1/imagens-puzzle1/cenas-introducao/icone_ocp.png')
        pygame.display.set_icon(icone)

        # Carrega a imagem de fundo:
        self.fundo = pygame.image.load('puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta.png')
        self.fundo = pygame.transform.scale(self.fundo, (self.largura_janela, self.altura_janela))

        # Carrega o fragmento de chave (coletável):
        self.imagem_fragmento_1 = pygame.image.load('puzzle1/imagens-puzzle1/imagens-coleta/fragmento-1.png')
        self.imagem_fragmento_1 = pygame.transform.scale(self.imagem_fragmento_1, (100, 100))

        # Define a posição do fragmento de chave (coletável) e seu retângulo de colisão:
        self.imagem_fragmento_1_x = 1100
        self.imagem_fragmento_1_y = 550
        self.rect_imagem_fragmento_1 = pygame.Rect(self.imagem_fragmento_1_x, self.imagem_fragmento_1_y, self.imagem_fragmento_1.get_width(), self.imagem_fragmento_1.get_height())

        # Carrega o som de coleta:
        self.som_coleta = pygame.mixer.Sound('puzzle1/sons-puzzle1/puzzle1-som-coleta.wav')

        # Carrega um espaço vazio que servirá para avançar de cena:
        self.colisao_avancar_fase = pygame.image.load('puzzle1/imagens-puzzle1/imagens-coleta/espaco-colisao-avancar-fase.png')
        self.colisao_avancar_fase = pygame.transform.scale(self.colisao_avancar_fase, (100, 100))

        # Define a posição do espaço vazio que servirá para avançar de cena e seu retângulo de colisão:
        self.colisao_avancar_fase_x = 1260
        self.colisao_avancar_fase_y = 550
        self.rect_colisao_avancar_fase = pygame.Rect(self.colisao_avancar_fase_x, self.colisao_avancar_fase_y, self.colisao_avancar_fase.get_width(), self.colisao_avancar_fase.get_height())

        # Inicializa o personagem:
        self.personagem = Personagem_1d(self.largura_janela // 2, self.altura_janela // 2, 10, 2.4)

        self.coletado = False
        self.avancar_fase = False

    # Função para mostrar as cenas de introdução da coleta:
    def cenas_iniciais(self):
        cenas = [
            'puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro1.png',
            'puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro2.png',
            'puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro3.png',
            'puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro4.png',
            'puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro5.png'
        ]

        for imagem_cena in cenas:
            cena = pygame.image.load(imagem_cena)
            cena = pygame.transform.scale(cena, (self.largura_janela, self.altura_janela))
            status_introducao = True

            while status_introducao:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            status_introducao = False

                self.tela.blit(cena, (0, 0))
                self.visualizar_infos_coletaveis()
                pygame.display.flip()

    def loop(self):
        status_coleta = True
        while status_coleta:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    status_coleta = False

            tecla = pygame.key.get_pressed()

            self.personagem.mover(tecla)

            # Verifica a colisão entre o personagem e o fragmento de chave:
            if not self.coletado and self.personagem.rect.colliderect(self.rect_imagem_fragmento_1):
                infos_coletaveis.qtd_fragmento_1 += 1
                self.som_coleta.play()
                self.coletado = True

            # Desenha o fundo:
            self.tela.blit(self.fundo, (0, 0))

            # Desenha o fragmento de chave se ele não tiver sido coletado:
            if not self.coletado:
                self.tela.blit(self.imagem_fragmento_1, (self.imagem_fragmento_1_x, self.imagem_fragmento_1_y))

            # Verifica a colisão entre o personagem e o espaço de avançar de fase:
            if not self.avancar_fase and self.personagem.rect.colliderect(self.rect_colisao_avancar_fase):
                comecar_puzzle2()
                self.avancar_fase = True
                status_coleta = False

            # "Desenha" o espaço para a colisão entre o personagem e o espaço de avançar de fase:
            if not self.avancar_fase:
                self.tela.blit(self.colisao_avancar_fase, (self.colisao_avancar_fase_x, self.colisao_avancar_fase_y))

            # Desenha o personagem:
            self.personagem.desenhar(self.tela)

            self.visualizar_infos_coletaveis()
            # Atualiza a tela:
            pygame.display.flip()

            # Controla a taxa de atualização:
            pygame.time.Clock().tick(50)

        pygame.quit()
        sys.exit()

    def visualizar_infos_coletaveis(self):
        view_infos_coletaveis = pygame.image.load('puzzle1/visualizacao_coletaveis.png')
        self.tela.blit(view_infos_coletaveis, (10, 220))

        fonte = pygame.font.SysFont('freesansbold.ttf', 70)

        txt_info_cracha = fonte.render(str(infos_coletaveis.qtd_cracha), True, (255, 255, 255))
        self.tela.blit(txt_info_cracha, (80, 235))

        txt_info_fragmento_2 = fonte.render(str(infos_coletaveis.qtd_fragmento_2), True, (255, 255, 255))
        self.tela.blit(txt_info_fragmento_2, (80, 312))

        txt_info_fragmento_1 = fonte.render(str(infos_coletaveis.qtd_fragmento_1), True, (255, 255, 255))
        self.tela.blit(txt_info_fragmento_1, (80, 388))

        pygame.display.flip()

# Função para começar a coleta (chamada em outro arquivo):
def comecar_coleta():
    pygame.mixer.music.load('puzzle1/sons-puzzle1/som-musica-fundo.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.8)

    jogo.cenas_iniciais() # Mostra as imagens introdutórias
    jogo.loop() # Executa a coleta de fato

jogo = Jogo()
