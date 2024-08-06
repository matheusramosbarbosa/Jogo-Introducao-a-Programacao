import pygame
import sys
from personagem_coleta import Personagem

status_coleta = False

# Define a classe da coleta:
class Coleta:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1280
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')

        # Carrega a imagem de fundo:
        self.fundo = pygame.image.load('puzzle 2/graphics/cena-coleta.png')
        self.fundo = pygame.transform.scale(self.fundo, (self.largura_janela, self.altura_janela))

        # Carrega o fragmento de chave (coletável):
        self.imagem_fragmento_1 = pygame.image.load('puzzle 2/graphics/fragmento-2.png')
        self.imagem_fragmento_1 = pygame.transform.scale(self.imagem_fragmento_1, (100, 100))

        # Define a posição do fragmento de chave (coletável) e seu retângulo de colisão:
        self.imagem_fragmento_1_x = 900
        self.imagem_fragmento_1_y = 550
        self.rect_imagem_fragmento_1 = pygame.Rect(self.imagem_fragmento_1_x, self.imagem_fragmento_1_y, self.imagem_fragmento_1.get_width(), self.imagem_fragmento_1.get_height())

        # Carrega o som de coleta:
        self.som_coleta = pygame.mixer.Sound('puzzle 2/sounds/som-coleta.wav')

        # Define a posição do espaço vazio que servirá para avançar de cena e seu retângulo de colisão:
        self.colisao_avancar_fase_x = 1260
        self.colisao_avancar_fase_y = 550
        self.rect_colisao_avancar_fase = pygame.Rect(self.colisao_avancar_fase_x, self.colisao_avancar_fase_y, 200, 200)

        # Inicializa o personagem:
        self.personagem = Personagem(self.largura_janela // 2, self.altura_janela // 2, 10, 2.4)

        self.coletado = False
        self.avancar_fase = False

    def cenas_iniciais(self):
        cenas = [
            'puzzle 2/graphics/cena-coleta-1.png',
            'puzzle 2/graphics/cena-coleta-2.png',
            'puzzle 2/graphics/cena-coleta-3.png',
            'puzzle 2/graphics/cena-coleta-4.png',
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
                self.som_coleta.play()
                self.coletado = True

            # Desenha o fundo:
            self.tela.blit(self.fundo, (0, 0))

            # Desenha o fragmento de chave se ele não tiver sido coletado:
            if not self.coletado:
                self.tela.blit(self.imagem_fragmento_1, (self.imagem_fragmento_1_x, self.imagem_fragmento_1_y))

            # Verifica a colisão entre o personagem e o espaço de avançar de fase:
            if not self.avancar_fase and self.personagem.rect.colliderect(self.rect_colisao_avancar_fase):
                self.avancar_fase = True
                status_coleta = False

            # Desenha o personagem:
            self.personagem.desenhar(self.tela)

            # Atualiza a tela:
            pygame.display.flip()

            # Controla a taxa de atualização:
            pygame.time.Clock().tick(50)

        pygame.quit()
        sys.exit()

# Função para começar a coleta (chamada em outro arquivo):
def comecar_coleta():
    pygame.mixer.music.load('puzzle 2/sounds/Pokemon FireRedLeafGreen- Pokemon Center.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    jogo = Coleta()
    jogo.cenas_iniciais()
    jogo.loop() # Executa a coleta de fatoc