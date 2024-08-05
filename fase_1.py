import pygame
from sys import exit


#Cria a classe Movel, que contem todos os atributos e comportamentos de um movel
class Movel():
    def __init__(self, x, y, surf, casa, escala):
        #Posição (x,y) e o tamanho da casa (quantidade de pixels) que ele anda
        self.x = x
        self.y = y
        self.casa = casa
        self.surface = pygame.transform.scale(surf, (surf.get_width() * escala, surf.get_height() * escala))
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
    def __init__(self, x, y, casa, escala):
        self.x = x
        self.y = y
        self.casa = casa

        self.imagens = {'frente' : pygame.transform.scale(pygame.image.load('graphics/prota-frente-0.png'), (pygame.image.load('graphics/prota-frente-0.png').get_width() * escala, pygame.image.load('graphics/prota-frente-0.png').get_height() * escala)),
                        'costas' : pygame.transform.scale(pygame.image.load('graphics/prota-costas-0.png'), (pygame.image.load('graphics/prota-costas-0.png').get_width() * escala, pygame.image.load('graphics/prota-costas-0.png').get_height() * escala)),
                        'direita' : pygame.transform.scale(pygame.image.load('graphics/prota-direita-0.png'), (pygame.image.load('graphics/prota-direita-0.png').get_width() * escala, pygame.image.load('graphics/prota-direita-0.png').get_height() * escala)),
                        'esquerda': pygame.transform.scale(pygame.image.load('graphics/prota-esquerda-0.png'), (pygame.image.load('graphics/prota-esquerda-0.png').get_width() * escala, pygame.image.load('graphics/prota-esquerda-0.png').get_height() * escala))}
       
        self.surf = self.imagens['frente']    
        self.rect = pygame.Rect(self.x, self.y, self.surf.get_width(), self.surf.get_height())

        #É necessario essas flags pra diferenciar as colisão entre Personagem e Movel
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def movimento(self, direcao):
        if direcao == 'direita':
            self.rect.x += self.casa
            self.move_direita = True
            self.surf = self.imagens['direita']
        if direcao == 'esquerda':
            self.rect.x -= self.casa
            self.move_esquerda = True
            self.surf = self.imagens['esquerda']
        if direcao == 'baixo':
            self.rect.y += self.casa
            self.move_baixo = True
            self.surf = self.imagens['frente']
        if direcao == 'cima':
            self.rect.y -= self.casa
            self.move_cima = True
            self.surf = self.imagens['costas']

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
        
        self.fonte_text = pygame.font.Font('Pixeltype.ttf', 100)
        self.text_surf = self.fonte_text.render('R = Reiniciar', False, 'White')

        self.fase = 1

        self.mapa = pygame.image.load('graphics/fase_1.png')
        #Criação das dos retangulso das paredes, pra poder haver colisão
        self.paredes_cima = [Parede(470,150, 340,40), Parede(230,270, 220,40), Parede(830,270, 220,40)]
        self.paredes_baixo = [Parede(470,530, 340,40), Parede(230, 410, 220,40), Parede(830,410, 220,40)]
        self.paredes_esquerda = [Parede(430,190, 40,100), Parede(430,430, 40,100), Parede(190,310, 40,100)]
        self.paredes_direita = [Parede(810,190, 40,100), Parede(810,430, 40,100), Parede(1050,310, 40,100)]

        #Criação do retangulo da casa onde o personagem precisa empurrar os moveis
        self.objetivos = [Objetivo(230,310, 100,100), Objetivo(950,310, 100,100)]

        #Criação do personagem e dos moveis
        self.personagem = Personagem(590,190, 120, 1)
        self.moveis = [Movel(470, 310, pygame.image.load('graphics/armario_hospital.png') ,120, 2),
                        Movel(710, 310, pygame.image.load('graphics/armario_hospital.png'), 120, 2)]

        self.som_acerto = pygame.mixer.Sound('sounds/acerto_sound_effect.mp3')
        self.nao_tocou = True
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
                    self.personagem.rect.x += self.personagem.casa
                if self.personagem.move_direita:
                    self.personagem.rect.x -= self.personagem.casa
                if self.personagem.move_cima:
                    self.personagem.rect.y += self.personagem.casa
                if self.personagem.move_baixo:
                    self.personagem.rect.y -= self.personagem.casa
            
       
            
                    

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
                
            



    def mudar_fase(self, fase):
        if fase == 2:
            self.mapa = pygame.image.load('graphics/fase_2.png')
            self.fase = 2
            self.personagem = Personagem(525,365, 60, 0.5)
            self.moveis = [Movel(585,365, pygame.image.load('graphics/maca_hospital.png'),60, 1), 
                           Movel(405,245, pygame.image.load('graphics/armario_hospital.png'), 60,1),
                           Movel(825,185, pygame.image.load('graphics/aparelho_hospital.png'),60,1)] 

            self.paredes_cima = [Parede(405,105, 470,20), Parede(345,225,50,20), Parede(465,345, 170,20),
                                 Parede(705,345, 110,20), Parede(885,465, 50,20), Parede(585,525, 230,20)]
            self.paredes_baixo = [Parede(465,175, 170,20), Parede(705,175, 110,20), Parede(345,415, 50,20),
                                  Parede(465,415, 350,20), Parede(405,535, 50,20), Parede(585,595, 350,20)]
            self.paredes_esquerda = [Parede(385,125, 20,110)]
            self.paredes_direita = []   



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
                    
            keys = pygame.key.get_pressed()
            
       
            if self.fase == 1:
                self.tela.fill((18,18,18))
                self.tela.blit(self.mapa, (210,170))
                
                if keys[pygame.K_r]:
                    self.personagem = Personagem(590,190, 120, 1)
                    self.moveis = [Movel(470, 310, pygame.image.load('graphics/armario_hospital.png') ,120, 2),
                                   Movel(710, 310, pygame.image.load('graphics/armario_hospital.png'), 120, 2)]


                self.colisao_moveis()
                self.colisao_paredes()  

                self.personagem.desenhar_personagem(self.tela)
                for movel in self.moveis:
                    movel.desenhar_movel(self.tela)
                    movel.reset_movimento()

                self.personagem.reset_movimento()
               
                if self.moveis[0].rect.colliderect(self.objetivos[0]) and self.moveis[1].rect.colliderect(self.objetivos[1]):
                    if self.nao_tocou:
                        self.som_acerto.play()
                        self.nao_tocou = False
                        self.mudar_fase(2)
            
            if self.fase == 2:
                self.tela.fill((18,18,18))
                self.tela.blit(self.mapa, (335,115))

                self.colisao_moveis()
                self.colisao_paredes()  
            

                pygame.draw.rect(self.tela, (32,255, 20), self.personagem.rect)
                pygame.draw.rect(self.tela, (32,255, 20), self.moveis[2])
                pygame.draw.rect(self.tela, (255,255, 32), self.paredes_esquerda[0])
                self.personagem.desenhar_personagem(self.tela)
                for movel in self.moveis:
                    movel.desenhar_movel(self.tela)
                    movel.reset_movimento()
                self.personagem.reset_movimento()
                
            self.tela.blit(self.text_surf, (100, 60)) 
            pygame.display.flip()
            self.clock.tick(60)


puzzle = Fase_1()
puzzle.loop()
        

        
        
