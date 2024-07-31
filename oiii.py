import pygame
import sys


class Personagem:
    def __init__(self, x, y, velocidade, escala):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.direcao = 'frente'
        self.passo = 0
        self.contador_passos = 0
        self.escala = escala
        self.movimento = False

        # Carregar imagens do personagem
        self.imagens = {
            'tras': [pygame.transform.scale(pygame.image.load('sergio-costas-sem2.png'), (
            pygame.image.load('sergio-costas-sem2.png').get_width() * escala,
            pygame.image.load('sergio-costas-sem2.png').get_height() * escala)),
                     pygame.transform.scale(pygame.image.load('img_1.png'), (
                     pygame.image.load('img_1.png').get_width() * escala,
                     pygame.image.load('img_1.png').get_height() * escala))],
            'frente': [pygame.transform.scale(pygame.image.load('sergio-frente-com-cracha2.png'), (
            pygame.image.load('sergio-frente-com-cracha2.png').get_width() * escala, pygame.image.load('sergio-frente-com-cracha2.png').get_height() * escala)),
                       pygame.transform.scale(pygame.image.load('sergio-frente-com-cracha1.png'), (
                       pygame.image.load('sergio-frente-com-cracha1.png').get_width() * escala,
                       pygame.image.load('sergio-frente-com-cracha1.png').get_height() * escala))],
            'esquerda': [pygame.transform.scale(pygame.image.load('img_2.png'), (
            pygame.image.load('img_2.png').get_width() * escala, pygame.image.load('img_2.png').get_height() * escala)),
                         pygame.transform.scale(pygame.image.load('img_2.png'), (
                         pygame.image.load('img_2.png').get_width() * escala,
                         pygame.image.load('img_2.png').get_height() * escala))],
            'direita': [pygame.transform.scale(pygame.image.load('direita 1.png'), (
            pygame.image.load('direita 1.png').get_width() * escala, pygame.image.load('direita 1.png').get_height() * escala)),
                        pygame.transform.scale(pygame.image.load('sergio-direita-sem2.png'), (
                        pygame.image.load('sergio-direita-sem2.png').get_width() * escala,
                        pygame.image.load('sergio-direita-sem2.png').get_height() * escala))]
        }

        # Imagens paradas
        self.imagens_parado = {
            'frente': pygame.transform.scale(pygame.image.load('sergio-frente-com0.png'), (
            pygame.image.load('sergio-frente-com0.png').get_width() * escala, pygame.image.load('sergio-frente-com0.png').get_height() * escala)),
            'tras': pygame.transform.scale(pygame.image.load('sergio-costas-cracha0.png'), (
            pygame.image.load('sergio-costas-cracha0.png').get_width() * escala,
            pygame.image.load('sergio-costas-cracha0.png').get_height() * escala)),
            'esquerda': pygame.transform.scale(pygame.image.load('sergio-esqueda-sem0.png'), (
            pygame.image.load('sergio-esqueda-sem0.png').get_width() * escala, pygame.image.load('sergio-esqueda-sem0.png').get_height() * escala)),
            'direita': pygame.transform.scale(pygame.image.load('sergio-direita-com0.png'), (
            pygame.image.load('sergio-direita-com0.png').get_width() * escala,
            pygame.image.load('sergio-direita-com0.png').get_height() * escala))
        }

    def mover(self, teclas):
        self.movimento = False
        if teclas[pygame.K_a]:
            self.x -= self.velocidade
            self.direcao = 'esquerda'
            self.movimento = True
        if teclas[pygame.K_d]:
            self.x += self.velocidade
            self.direcao = 'direita'
            self.movimento = True
        if teclas[pygame.K_w]:
            self.y -= self.velocidade
            self.direcao = 'tras'
            self.movimento = True
        if teclas[pygame.K_s]:
            self.y += self.velocidade
            self.direcao = 'frente'
            self.movimento = True

        # Alternar entre as imagens de passo
        if self.movimento:
            self.contador_passos += 1
            if self.contador_passos >= 10:
                self.passo = (self.passo + 1) % 2
                self.contador_passos = 0

    def desenhar(self, tela, largura_janela, altura_janela):
        if self.movimento:
            tela.blit(self.imagens[self.direcao][self.passo], (largura_janela // 2, altura_janela // 2))
        else:
            tela.blit(self.imagens_parado[self.direcao], (largura_janela // 2, altura_janela // 2))


class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1280    
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        pygame.display.set_caption("Movimento do Personagem")

        # Carregar a imagem de fundo
        self.fundo = pygame.image.load('img_9.png')
        self.fundo_largura = self.fundo.get_width()
        self.fundo_altura = self.fundo.get_height()

        # Inicializar o personagem
        self.personagem = Personagem(self.largura_janela // 2, self.altura_janela // 2, 5, 2)

    def atualizar_fundo(self, camera_x, camera_y):
        # Desenhar o fundo repetidamente para cobrir toda a tela
        for i in range(-self.fundo_largura, self.largura_janela + self.fundo_largura, self.fundo_largura):
            for j in range(-self.fundo_altura, self.altura_janela + self.fundo_altura, self.fundo_altura):
                self.tela.blit(self.fundo, (i - camera_x % self.fundo_largura, j - camera_y % self.fundo_altura))

    def loop(self):
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            teclas = pygame.key.get_pressed()

            self.personagem.mover(teclas)

            # Calcular a posição da câmera para centralizar o personagem
            camera_x = self.personagem.x - self.largura_janela // 2
            camera_y = self.personagem.y - self.altura_janela // 2

            self.atualizar_fundo(camera_x, camera_y)
            self.personagem.desenhar(self.tela, self.largura_janela, self.altura_janela)

            # Atualizar a tela
            pygame.display.flip()

            # Controlar a taxa de atualização
            pygame.time.Clock().tick(50)

        pygame.quit()
        sys.exit()


jogo = Jogo()
jogo.loop()
