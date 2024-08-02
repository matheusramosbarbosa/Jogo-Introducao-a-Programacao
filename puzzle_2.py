import pygame
from sys import exit

#Cria a classe Movel, que contem todos os atributos e comportamentos de um movel
class Movel():
    def __init__(self, x, y, surf, casa):
        #Posição (x,y) e o tamanho da casa que ele anda
        self.x = x
        self.y = y
        self.casa = casa

        self.surface = pygame.transform.scale(surf, ((surf.get_width()+8) * 2, surf.get_height() * 2))
        self.rect = pygame.Rect(self.x, self.y, self.surface.get_width(), self.surface.get_height() )

        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def movimento_movel(self, direcao):
        if direcao == 'direita':
            self.rect.x += self.casa
        if direcao == 'esquerda':
            self.rect.x -= self.casa
        if direcao == 'cima':
            self.rect.y -= self.casa
        if direcao == 'baixo':
            self.rect.y += self.casa

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
class Puzzle_2:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1280
        self.altura_janela = 720
        self.tela = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        self.clock = pygame.time.Clock()

        self.mapa_1 = pygame.image.load('graphics/fase_1.png')
        self.mapa_1 = pygame.transform.scale(self.mapa_1, (self.mapa_1.get_width() , self.mapa_1.get_height() ))

        self.paredes = [Parede(470,170,340,20)]

        self.objetivos = [Objetivo(230,310,100,100)]

        self.personagem = Personagem(590,190, 120)
        self.armario = Movel(470, 310, pygame.image.load('graphics/armario_hospital.png') ,120)

        self.som_acerto = pygame.mixer.Sound('sounds/acerto_sound_effect.mp3')

    def loop(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_d:
                        self.personagem.movimento('direita')
                    if evento.key == pygame.K_a:
                        self.personagem.movimento('esquerda')
                    if evento.key == pygame.K_s:
                        self.personagem.movimento('baixo')
                    if evento.key == pygame.K_w:
                        self.personagem.movimento('cima')

            self.tela.fill((18,18,18))
            self.tela.blit(self.mapa_1, (210,170))
            
            self.personagem.desenhar_personagem(self.tela)
            self.armario.desenhar_movel(self.tela)

            pygame.draw.rect(self.tela, (50,50,50), self.paredes[0].rect)
            if self.armario.rect.collidelist(self.objetivos) != -1:
                self.som_acerto.play()

            if self.personagem.rect.colliderect(self.armario.rect):
                if self.personagem.move_esquerda:
                    self.armario.movimento_movel('esquerda')
                if self.personagem.move_direita:
                    self.armario.movimento_movel('direita')
                if self.personagem.move_cima:
                    self.armario.movimento_movel('cima')
                if self.personagem.move_baixo:
                    self.armario.movimento_movel('baixo')

            


            self.personagem.reset_movimento()

            pygame.display.flip()
            self.clock.tick(60)


puzzle = Puzzle_2()
puzzle.loop()
        

        
        
