import pygame
import sys

pygame.init()
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')
icone = pygame.image.load('puzzle1/imagens-puzzle1/cenas-introducao/icone_ocp.png')
pygame.display.set_icon(icone)
fundo = pygame.image.load('graficos/tela_inicio/imagens/inicio.png')

# Define e executa a música de fundo em um loop infinito:
pygame.mixer.music.load('puzzle1/sons-batalha/mus_introcar.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

class Botao():
    def __init__(self, imagem, x_pos, y_pos, largura_hitbox=None, altura_hitbox=None):
        self.imagem = imagem
        self.imagem_original = imagem
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.imagem_rect = self.imagem.get_rect(center=(self.x_pos, self.y_pos))

        # Ajusta o retângulo/hitbox ao tamanho desejado
        if largura_hitbox and altura_hitbox:
            self.hitbox_rect = pygame.Rect(
                self.imagem_rect.centerx - largura_hitbox // 2, 
                self.imagem_rect.centery - altura_hitbox // 2, 
                largura_hitbox, 
                altura_hitbox
            )
        else:
            self.hitbox_rect = self.imagem_rect
        
    def update(self):
        tela.blit(self.imagem, self.imagem_rect)
        
    def checar_clique(self, pos):
        if self.hitbox_rect.collidepoint(pos):
            return True
        return False
    
    def mudar_imagem(self, pos, imagem_press):
        if self.hitbox_rect.collidepoint(pos):
            self.imagem = imagem_press
        else:
            # Volta para a imagem original
            self.imagem = self.imagem_original

bt_1 = pygame.image.load('graficos/tela_inicio/imagens/bt1.png')
bt_1_press = pygame.image.load('graficos/tela_inicio/imagens/bt1_2.png')
bt_2 = pygame.image.load('graficos/tela_inicio/imagens/bt2.png')
bt_2_press = pygame.image.load('graficos/tela_inicio/imagens/bt2_2.png')
bt_3 = pygame.image.load('graficos/tela_inicio/imagens/bt3.png')

# Definindo hitboxes personalizadas
botao_um = Botao(bt_1, 640, 405, largura_hitbox=280, altura_hitbox=180)
botao_dois = Botao(bt_2, 640, 595, largura_hitbox=280, altura_hitbox=96)
botao_tres = Botao(bt_3, 640, 690, largura_hitbox=150, altura_hitbox=30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botao_um.checar_clique(pygame.mouse.get_pos()):
                with open('main.py', 'r') as file:
                    arquivo = file.read()
                    exec(arquivo)
            if botao_dois.checar_clique(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            if botao_tres.checar_clique(pygame.mouse.get_pos()):
                print("Botão 3 pressionado!")

    tela.blit(fundo, (0, 0))  # Desenha o fundo antes de desenhar os botões
    botao_dois.mudar_imagem(pygame.mouse.get_pos(), bt_2_press)
    botao_um.mudar_imagem(pygame.mouse.get_pos(), bt_1_press)
    botao_tres.update()
    botao_dois.update()
    botao_um.update()

    pygame.display.update()
