import pygame
import sys
from puzzle1.objeto_personagem_2d import Personagem

pygame.init()
iniciar_teste = False

class Jogo:
    def carregar_jogo(self):
        print('teste')
        self.largura_janela = 1280
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        pygame.display.set_caption('OPC: Teste de locomoção do personagem 2d')

        # Carrega a imagem de fundo:
        self.fundo = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-coleta/cena-cin-ufpe.png')
        self.fundo_largura = self.fundo.get_width()
        self.fundo_altura = self.fundo.get_height()

        # Inicializa o personagem:
        self.personagem = Personagem(self.largura_janela // 2, self.altura_janela // 2, 5, 2)

    def atualizar_fundo(self, camera_x, camera_y):
        # Desenhar o fundo repetidamente para cobrir toda a tela:
        for i in range(-self.fundo_largura, self.largura_janela + self.fundo_largura, self.fundo_largura):
            for j in range(-self.fundo_altura, self.altura_janela + self.fundo_altura, self.fundo_altura):
                self.tela.blit(self.fundo, (i - camera_x % self.fundo_largura, j - camera_y % self.fundo_altura))

    def loop(self):
        status_loop = True
        while status_loop:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    status_loop = False

            tecla = pygame.key.get_pressed()

            self.personagem.mover(tecla)

            # Calcula a posição da câmera para centralizar o personagem:
            camera_x = self.personagem.x - self.largura_janela // 2
            camera_y = self.personagem.y - self.altura_janela // 2

            self.atualizar_fundo(camera_x, camera_y)
            self.personagem.desenhar(self.tela, self.largura_janela, self.altura_janela)

            # Atualiza a tela:
            pygame.display.flip()

            # Controla a taxa de atualização:
            pygame.time.Clock().tick(50)

        pygame.quit()
        sys.exit()

def rodar_jogo():
    jogo = Jogo()
    jogo.carregar_jogo()
    jogo.loop()