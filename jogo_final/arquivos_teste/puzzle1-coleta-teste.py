import pygame
import sys
from objetos_personagem import Personagem


# Define a classe do Jogo:
class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1280
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')

        # Carrega a imagem de fundo:
        self.fundo = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta.png')
        self.fundo = pygame.transform.scale(self.fundo, (self.largura_janela, self.altura_janela))

        # Carrega o fragmento de chave (coletável):
        self.imagem_estatica = pygame.image.load('../puzzle1/imagens-puzzle1/imagens-coleta/fragmento-1.png')
        self.imagem_estatica = pygame.transform.scale(self.imagem_estatica, (100, 100))

        # Define a posição do fragmento de chave (coletável) e seu retângulo de colisão:
        self.imagem_estatica_x = 1100
        self.imagem_estatica_y = 550
        self.rect_imagem_estatica = pygame.Rect(self.imagem_estatica_x, self.imagem_estatica_y,
                                                self.imagem_estatica.get_width(), self.imagem_estatica.get_height())

        # Carrega o som de coleta:
        self.som_conquista = pygame.mixer.Sound('../puzzle1/sons-puzzle1/puzzle1-som-coleta.mp3')

        # Inicializa o personagem:
        self.personagem = Personagem(self.largura_janela // 2, self.altura_janela // 2, 10, 10)

        self.coletado = False

    # Função para mostrar as cenas de introdução da coleta:
    def cenas_iniciais(self):
        cenas = [
            'imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro1.png',
            'imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro2.png',
            'imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro3.png',
            'imagens-puzzle1/cenas-coleta/puzzle1-cena-coleta-intro4.png'
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
            if not self.coletado and self.personagem.rect.colliderect(self.rect_imagem_estatica):
                self.som_conquista.play()
                self.coletado = True

            # Desenha o fundo:
            self.tela.blit(self.fundo, (0, 0))

            # Desenha o fragmento de chave se ele não tiver sido coletado:
            if not self.coletado:
                self.tela.blit(self.imagem_estatica, (self.imagem_estatica_x, self.imagem_estatica_y))

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
    jogo = Jogo()
    jogo.cenas_iniciais() # Mostra as imagens introdutórias
    jogo.loop() # Executa a coleta de fato
