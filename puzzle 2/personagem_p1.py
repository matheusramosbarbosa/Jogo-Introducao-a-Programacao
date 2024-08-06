import pygame

# Define a classe do personagem, com as características do objeto:
class Personagem:
    # Define a função de incialização do objeto Personagem:
    def __init__(self, x, y, velocidade, escala):
        self.x = y - 200
        self.y = y + 80
        self.velocidade = velocidade
        self.direcao = 'frente'
        self.passo = 0
        self.contador_passos = 0
        self.escala = escala
        self.movimento = False

        # Carrega as imagens do personagem em movimento:
        self.imagens = {
            'esquerda':
                [pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-esquerda-1.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-esquerda-1.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-esquerda-1.png').get_height() * escala)), pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-esquerda-2.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-esquerda-2.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-esquerda-2.png').get_height() * escala))],

            'direita':
                [pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-direita-1.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-direita-1.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-direita-1.png').get_height() * escala)), pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-direita-2.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-direita-2.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-anda-direita-2.png').get_height() * escala))]
        }

        # Carrega as imagens do personagem parado:
        self.imagens_parado = {
            'frente':
                pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-frente.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-frente.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-frente.png').get_height() * escala)),

            'esquerda':
                pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-esquerda.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-esquerda.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-esquerda.png').get_height() * escala)),

            'direita':
                pygame.transform.scale(pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-direita.png'),
           (pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-direita.png').get_width() * escala, pygame.image.load('imagens-puzzle1/imagens-coleta/personagem-direita.png').get_height() * escala))
        }

        # Definir o retângulo do personagem
        self.rect = pygame.Rect(self.x, self.y, self.imagens['direita'][0].get_width(), self.imagens['direita'][0].get_height())

    # Função para mover o personagem:
    def mover(self, tecla):
        self.movimento = False

        if tecla[pygame.K_a] and self.rect.left > 0:
            self.x -= self.velocidade
            self.direcao = 'esquerda'
            self.movimento = True

        elif tecla[pygame.K_d] and self.rect.right < 1280:
            self.x += self.velocidade
            self.direcao = 'direita'
            self.movimento = True

        # Alterna entre as imagens do passo:
        if self.movimento:
            self.contador_passos += 1
            if self.contador_passos >= 10:
                self.passo = (self.passo + 1) % 2
                self.contador_passos = 0

        # Atualiza o retângulo do personagem:
        self.rect.topleft = (self.x, self.y)

    # Função para desenhar o personagem:
    def desenhar(self, tela):
        if self.movimento:
            tela.blit(self.imagens[self.direcao][self.passo], (self.x, self.y))
        else:
            tela.blit(self.imagens_parado[self.direcao], (self.x, self.y))