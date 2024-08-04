import pygame
from sys import exit

#Cria a classe Movel, que contem todos os atributos e comportamentos de um movel
class Movel():
    def __init__(self, x, y, surf, casa):
        #Posição (x,y) e o tamanho da casa (quantidade de pixels) que ele anda
        self.x = x
        self.y = y
        self.casa = casa

        self.surface = pygame.transform.scale(surf, (surf.get_width() * 2, surf.get_height() * 2))
        self.rect = pygame.Rect(self.x, self.y, self.surface.get_width(), self.surface.get_height() )

        #É necessario essas flags pra diferenciar as colisão entre Personagem e Movel
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False
    #Movimentação do movel
    def movimento_movel(self, direcao):
        if direcao == 'direita':
            self.rect.x += self.casa
            self.move_direita = True
        if direcao == 'esquerda':
            self.rect.x -= self.casa
            self.move_esquerda = True
        if direcao == 'cima':
            self.rect.y -= self.casa
            self.move_cima = True
        if direcao == 'baixo':
            self.rect.y += self.casa
            self.move_baixo = True
    
    def reset_movimento(self):
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def desenhar_movel(self, tela):
        tela.blit(self.surface, self.rect)

#Personagem
class Personagem:
    def __init__(self, x, y, casa):
        self.x = x
        self.y = y
        self.casa = casa

        self.surf = pygame.image.load('graphics/personagem_principal.png')
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

        #É necessario essas flags pra diferenciar as colisão entre Personagem e Movel
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def movimento(self, direcao):
        if direcao == 'direita':
            self.rect.x += self.casa
            self.move_direita = True
        if direcao == 'esquerda':
            self.rect.x -= self.casa
            self.move_esquerda = True
        if direcao == 'baixo':
            self.rect.y += self.casa
            self.move_baixo = True
        if direcao == 'cima':
            self.rect.y -= self.casa
            self.move_cima = True

    def reset_movimento(self):
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def desenhar_personagem(self,tela):
        tela.blit(self.surf, self.rect)

#Paredes
class Parede:
    def __init__(self,x,y,largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(self.x,self.y,self.largura,self.altura)

class Objetivo(Parede):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)

#Jogo
class Fase_1:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1280
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        self.clock = pygame.time.Clock()

        self.mapa = pygame.image.load('graphics/fase_1.png')
        #Criação das dos retangulso das paredes, pra poder haver colisão
        self.paredes_cima = [Parede(470,150, 340,40), Parede(230,270, 220,40), Parede(830,270, 220,40)]
        self.paredes_baixo = [Parede(470,530, 340,40), Parede(230, 410, 220,40), Parede(830,410, 220,40)]
        self.paredes_esquerda = [Parede(430,190, 40,100), Parede(430,430, 40,100), Parede(190,310, 40,100)]
        self.paredes_direita = [Parede(810,190, 40,100), Parede(810,430, 40,100), Parede(1050,310, 40,100)]

        #Criação do retangulo da casa onde o personagem precisa empurrar os moveis
        self.objetivos = [Objetivo(230,310, 100,100), Objetivo(950,310, 100,100)]

        #Criação do personagem e dos moveis
        self.personagem = Personagem(590,190, 120)
        self.armario_1 = Movel(470, 310, pygame.image.load('graphics/armario_hospital.png') ,120)
        self.armario_2 = Movel(710, 310, pygame.image.load('graphics/armario_hospital.png'), 120)
        self.moveis = [self.armario_1, self.armario_2]

        self.som_acerto = pygame.mixer.Sound('sounds/acerto_sound_effect.mp3')
    #Quando o personagem ou um objeto colidir com o retangulo da parede, faz com que ele retorne um passso, gerando o efeito de que ele nao pode passar dali
    def colisao_paredes(self):
        #Personagem/Parede:
        if self.personagem.rect.collidelist(self.paredes_direita) != -1 and self.personagem.move_direita:
            self.personagem.rect.x -= self.personagem.casa
        if self.personagem.rect.collidelist(self.paredes_esquerda) != -1 and self.personagem.move_esquerda:
            self.personagem.rect.x += self.personagem.casa
        if self.personagem.rect.collidelist(self.paredes_cima) != -1 and self.personagem.move_cima:
            self.personagem.rect.y += self.personagem.casa
        if self.personagem.rect.collidelist(self.paredes_baixo)!= -1 and self.personagem.move_baixo:
            self.personagem.rect.y -= self.personagem.casa

        #Objeto/Parede:
        for movel in self.moveis:
            if movel.rect.collidelist(self.paredes_direita) != -1 and movel.move_direita:
                movel.rect.x -= movel.casa
            if movel.rect.collidelist(self.paredes_esquerda) != -1 and movel.move_esquerda:
                movel.rect.x += movel.casa
            if movel.rect.collidelist(self.paredes_cima) != -1 and movel.move_cima:
                movel.rect.y += movel.casa
            if movel.rect.collidelist(self.paredes_baixo)!= -1 and movel.move_baixo:
                movel.rect.y -= movel.casa
            
            if movel.rect.colliderect(self.personagem.rect):
                if self.personagem.move_esquerda:
                    self.personagem.movimento('direita')
                if self.personagem.move_direita:
                    self.personagem.movimento('esquerda')
                if self.personagem.move_cima:
                    self.personagem.movimento('baixo')
                if self.personagem.move_baixo:
                    self.personagem.movimento('cima')

    #Colisão Personagem/Movel, fazendo com que o movel se mova na mesma direção que o personagem está indo
    def colisao_moveis(self):
        for movel in self.moveis:
            if self.personagem.rect.colliderect(movel.rect):
                if self.personagem.move_esquerda:
                    movel.movimento_movel('esquerda')
                if self.personagem.move_direita:
                    movel.movimento_movel('direita')
                if self.personagem.move_cima:
                    movel.movimento_movel('cima')
                if self.personagem.move_baixo:
                    movel.movimento_movel('baixo')


    def loop(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_d :
                        self.personagem.movimento('direita')
                    if evento.key == pygame.K_a:
                        self.personagem.movimento('esquerda')
                    if evento.key == pygame.K_s:
                        self.personagem.movimento('baixo')
                    if evento.key == pygame.K_w:
                        self.personagem.movimento('cima')

            self.tela.fill((18,18,18))
            self.tela.blit(self.mapa, (210,170))
        
            self.colisao_moveis()
            self.colisao_paredes()  

            self.personagem.desenhar_personagem(self.tela)
            self.armario_1.desenhar_movel(self.tela)
            self.armario_2.desenhar_movel(self.tela)
            
            self.personagem.reset_movimento()
            for movel in self.moveis:
                movel.reset_movimento()

            pygame.display.flip()
            self.clock.tick(60)


puzzle = Fase_1()
puzzle.loop()
        

        
        
