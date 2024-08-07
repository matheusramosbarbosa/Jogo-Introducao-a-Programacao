import pygame
from sys import exit
from puzzle2_coleta import comecar_coleta
from objetos_personagem import Infos_Coletaveis
from objetos_personagem import infos_coletaveis

pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')
icone = pygame.image.load('puzzle1\grapichs_puzzle2\icone_ocp.png')
pygame.display.set_icon(icone)

#Cria a classe Movel, que contem todos os atributos e comportamentos de um movel
class Movel():
    def __init__(self, x, y, surf, casa, escala):
        #Posição (x,y) e o tamanho da casa (quantidade de pixels) que ele anda
        self.x = x
        self.y = y
        self.casa = casa * escala
        
        self.surface = pygame.transform.scale(surf, (surf.get_width() * escala, surf.get_height() * escala))
        self.rect = pygame.Rect(self.x, self.y, self.surface.get_width(), self.surface.get_height() )

        #É necessario essas flags pra diferenciar as colisão entre Personagem e Movel
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False
    #Movimentação do movel
    def movimento_movel(self, direcao, escala):
        if direcao == 'direita':
            self.rect.x += 8 * escala
            self.move_direita = True
        if direcao == 'esquerda':
            self.rect.x -= 8 * escala
            self.move_esquerda = True
        if direcao == 'cima':
            self.rect.y -= 8 * escala
            self.move_cima = True
        if direcao == 'baixo':
            self.rect.y += 8 * escala
            self.move_baixo = True
    
    def reset_movimento(self):
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def desenhar_movel(self, tela):
        tela.blit(self.surface, self.rect)

# Função de movimentação do personagem própria para os desafios do Puzzle 2 (necessário):
class Personagem:
    def __init__(self, x, y, casa, escala):
        self.x = x
        self.y = y
        self.casa = casa * escala
        self.passos = 0
        self.imagens = {'frente-0' : pygame.transform.scale(pygame.image.load(
            'puzzle1/grapichs_puzzle2/personagem-frente.png'), (pygame.image.load(
            'puzzle1/grapichs_puzzle2/personagem-frente.png').get_width() * escala, pygame.image.load(
            'puzzle1/grapichs_puzzle2/personagem-frente.png').get_height() * escala)),
                        'frente-1' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-frente-1.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-frente-1.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-frente-1.png').get_height() * escala)),
                        'frente-2' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-frente-2.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-frente-2.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-frente-2.png').get_height() * escala)),
                        'costas-0' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-costas.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-costas.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-costas.png').get_height() * escala)),
                        'costas-1' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-costas-1.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-costas-1.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-costas-1.png').get_height() * escala)),
                        'costas-2' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-costas-2.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-costas-2.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-costas-2.png').get_height() * escala)),
                        'direita-0' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-direita.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-direita.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-direita.png').get_height() * escala)),
                        'direita-1' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-direita-1.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-direita-1.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-direita-1.png').get_height() * escala)),
                        'direita-2' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-direita-2.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-direita-2.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-direita-2.png').get_height() * escala)),
                        'esquerda-0': pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-esquerda.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-esquerda.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-esquerda.png').get_height() * escala)),
                        'esquerda-1': pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-esquerda-1.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-esquerda-1.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-esquerda-1.png').get_height() * escala)),
                        'esquerda-2' : pygame.transform.scale(pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-esquerda-2.png'), (pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-esquerda-2.png').get_width() * escala, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/personagem-anda-esquerda-2.png').get_height() * escala))}
       
        self.surf = self.imagens['frente-0']   
        self.rect = pygame.Rect(self.x, self.y, self.surf.get_width(), self.surf.get_height())

        #É necessario essas flags pra diferenciar as colisão entre Personagem e Movel
        self.move_direita = self.move_esquerda = self.move_cima = self.move_baixo = False

    def movimento(self, direcao, escala):
        if direcao == 'direita':
            if(self.passos<30):
                self.rect.x += 4 * escala
            self.passos += 1
            self.move_direita = True
            if(self.passos>10 and self.passos<21)or(self.passos>30):
                self.surf = self.imagens['direita-0']
            if(self.passos<11):
                self.surf = self.imagens['direita-1']
            if(self.passos>20 and self.passos<31):
                self.surf = self.imagens['direita-2']
        if direcao == 'esquerda':
            if(self.passos<30):
                self.rect.x -= 4 * escala
            self.passos += 1
            self.move_esquerda = True
            if(self.passos>10 and self.passos<21)or(self.passos>30):
                self.surf = self.imagens['esquerda-0']
            if(self.passos<11):
                self.surf = self.imagens['esquerda-1']
            if(self.passos>20 and self.passos<31):
                self.surf = self.imagens['esquerda-2']
        if direcao == 'baixo':
            if(self.passos<30):
                self.rect.y += 4 * escala
            self.passos += 1
            self.move_baixo = True
            if(self.passos>10 and self.passos<21)or(self.passos>30):
                self.surf = self.imagens['frente-0']
            if(self.passos<11):
                self.surf = self.imagens['frente-1']
            if(self.passos>20 and self.passos<31):
                self.surf = self.imagens['frente-2']
        if direcao == 'cima':
            if(self.passos<30):
                self.rect.y -= 4 * escala
            self.passos += 1
            self.move_cima = True
            if(self.passos>10 and self.passos<21)or(self.passos>30):
                self.surf = self.imagens['costas-0']
            if(self.passos<11):
                self.surf = self.imagens['costas-1']
            if(self.passos>20 and self.passos<31):
                self.surf = self.imagens['costas-2']

    

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

        self.fonte_text = pygame.font.Font('puzzle1/Pixeltype.ttf', 100)
        self.text_surf = self.fonte_text.render('R = Reiniciar', False, 'White')

        self.fase = 1
        self.resolucao = (210,155)

        self.mapa = pygame.image.load('puzzle1/grapichs_puzzle2/fase_1.png')
        #Criação das dos retangulso das paredes, pra poder haver colisão
        self.paredes_cima = [Parede(450,140, 340,40), Parede(230,260, 220,40), Parede(830,260, 220,40)]
        self.paredes_baixo = [Parede(470,540, 340,40), Parede(230, 420, 220,40), Parede(830,420, 220,40)]
        self.paredes_esquerda = [Parede(420,190, 40,100), Parede(420,430, 40,100), Parede(180,310, 40,100)]
        self.paredes_direita = [Parede(820,190, 40,100), Parede(820,430, 40,100), Parede(1060,310, 40,100)]

        #Criação do retangulo da casa onde o personagem precisa empurrar os moveis
        self.objetivos = [Objetivo(230,310, 100,100), Objetivo(950,310, 100,100)]

        #Criação do personagem e dos moveis
        self.personagem = Personagem(590,190, 120, 1)
        self.contagem = 0
        self.animação = False
        self.animaçãodireita = False
        self.animaçãoesquerda = False
        self.animaçãocima = False
        self.animaçãobaixo = False


        self.escala_movimento = 1

        self.movelsendocontado = 'nenhum'

        self.moveis = [Movel(470, 310, pygame.image.load('puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 2),
                       Movel(710, 310, pygame.image.load('puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 2)]

        self.som_acerto = pygame.mixer.Sound('puzzle1/sounds-puzzle2/acerto_sound_effect.mp3')
        self.nao_tocou = True
    #Quando o personagem ou um objeto colidir com o retangulo da parede, faz com que ele retorne um passso, gerando o efeito de que ele nao pode passar dali
    def colisao_paredes(self):
        #Personagem/Parede:
        if self.personagem.rect.collidelist(self.paredes_direita) != -1 and self.personagem.move_direita:
            self.personagem.rect.x -= self.personagem.casa
            return True
        if self.personagem.rect.collidelist(self.paredes_esquerda) != -1 and self.personagem.move_esquerda:
            self.personagem.rect.x += self.personagem.casa
            return True
        if self.personagem.rect.collidelist(self.paredes_cima) != -1 and self.personagem.move_cima:
            self.personagem.rect.y += self.personagem.casa
            return True
        if self.personagem.rect.collidelist(self.paredes_baixo)!= -1 and self.personagem.move_baixo:
            self.personagem.rect.y -= self.personagem.casa
            return True

        #Objeto/Parede:
        for movel in self.moveis:
            if movel.rect.collidelist(self.paredes_direita) != -1 and movel.move_direita:
                movel.rect.x -= movel.casa
                return True
            if movel.rect.collidelist(self.paredes_esquerda) != -1 and movel.move_esquerda:
                movel.rect.x += movel.casa
                return True
            if movel.rect.collidelist(self.paredes_cima) != -1 and movel.move_cima:
                movel.rect.y += movel.casa
                return True
            if movel.rect.collidelist(self.paredes_baixo)!= -1 and movel.move_baixo:
                movel.rect.y -= movel.casa
                return True
            
    def podeandar(self, objeto, direcao, émovel):
        if direcao == 'direita':
            objeto.rect.x += objeto.casa
            objeto.move_direita = True
            if self.colisao_paredes():
                return False
            for movel in self.moveis:
                if(movel!=objeto):
                    if(objeto.rect.colliderect(movel.rect)):
                        if(émovel =='sim'):
                            objeto.rect.x -= objeto.casa
                            return False
                        resultado = self.podeandar(movel, direcao, 'sim')
                        objeto.rect.x -= objeto.casa
                        return resultado
            objeto.rect.x -= objeto.casa
            return True
        if direcao == 'esquerda':
            objeto.rect.x -= objeto.casa
            objeto.move_esquerda = True
            if self.colisao_paredes():
                return False
            for movel in self.moveis:
                if(movel!=objeto):
                    if(objeto.rect.colliderect(movel.rect)):
                        if(émovel =='sim'):
                            objeto.rect.x += objeto.casa
                            return False
                        resultado = self.podeandar(movel, direcao, 'sim')
                        objeto.rect.x += objeto.casa
                        return resultado
            objeto.rect.x += objeto.casa
            return True
        if direcao == 'cima':
            objeto.rect.y -= objeto.casa
            objeto.move_cima = True
            if self.colisao_paredes():
                return False
            for movel in self.moveis:
                if(movel!=objeto):
                    if(objeto.rect.colliderect(movel.rect)):
                        if(émovel =='sim'):
                            objeto.rect.y += objeto.casa
                            return False
                        resultado = self.podeandar(movel, direcao, 'sim')
                        objeto.rect.y += objeto.casa
                        return resultado
            objeto.rect.y += objeto.casa
            return True
        if direcao == 'baixo':
            objeto.rect.y += objeto.casa
            objeto.move_baixo = True
            if self.colisao_paredes():
                return False
            for movel in self.moveis:
                if(movel!=objeto):
                    if(objeto.rect.colliderect(movel.rect)):
                        if(émovel =='sim'):
                            objeto.rect.y -= objeto.casa
                            return False
                        resultado = self.podeandar(movel, direcao, 'sim')
                        objeto.rect.y -= objeto.casa
                        return resultado
            objeto.rect.y -= objeto.casa
            return True

    #Colisão Personagem/Movel, fazendo com que o movel se mova na mesma direção que o personagem está indo
    def colisao_moveis(self):
        for movel in self.moveis:
            if (self.personagem.rect.colliderect(movel.rect))or(self.contagem>0 and self.movelsendocontado == movel):
                if self.personagem.move_esquerda:
                    movel.movimento_movel('esquerda', self.escala_movimento)
                    self.contagem += 1
                    self.movelsendocontado = movel
                    if(self.contagem==15):
                        self.contagem = 0
                        self.movelsendocontado = 'hehe ninguém'
                if self.personagem.move_direita:
                    movel.movimento_movel('direita', self.escala_movimento)
                    self.contagem += 1
                    self.movelsendocontado = movel
                    if(self.contagem==15):
                        self.contagem = 0
                        self.movelsendocontado = 'hehe ninguém'
                if self.personagem.move_cima:
                    movel.movimento_movel('cima', self.escala_movimento)
                    self.contagem += 1
                    self.movelsendocontado = movel
                    if(self.contagem==15):
                        self.contagem = 0
                        self.movelsendocontado = 'hehe ninguém'
                if self.personagem.move_baixo:
                    movel.movimento_movel('baixo', self.escala_movimento)
                    self.contagem += 1
                    self.movelsendocontado = movel
                    if(self.contagem==15):
                        self.contagem = 0
                        self.movelsendocontado = 'hehe ninguém'


    def mudar_fase(self, fase):
        if fase == 2:
            self.mapa = pygame.image.load('puzzle1/grapichs_puzzle2/fase_2.png')
            self.fase = 2
            self.resolucao = (335,120)
            self.escala_movimento = 0.5
            self.personagem = Personagem(525,395, 120, 0.5)
            self.moveis = [Movel(585, 395, pygame.image.load('puzzle1/grapichs_puzzle2/maca_hospital.png'), 60, 1),
                           Movel(405, 275, pygame.image.load('puzzle1/grapichs_puzzle2/aparelho_hospital.png'), 60, 1),
                           Movel(825, 215, pygame.image.load('puzzle1/grapichs_puzzle2/aparelho_hospital.png'), 60, 1)]

            self.paredes_cima = [Parede(405,135, 470,20), Parede(345,255,50,20), Parede(465,375, 170,20),
                                 Parede(705,375, 110,20), Parede(885,495, 50,20), Parede(585,555, 230,20)]
            self.paredes_baixo = [Parede(465,205, 170,20), Parede(705,205, 110,20), Parede(345,445, 50,20),
                                  Parede(465,445, 350,20), Parede(405,565, 50,20), Parede(585,625, 350,20)]
            self.paredes_esquerda = [Parede(385,155, 20,110),Parede(335+290,145+70, 20,170),Parede(335+470,145+70, 20,170),
                                     Parede(335-10,145+130, 20,170),Parede(335+50,145+310, 20,110),Parede(335+470,145+310, 20,110),
                                     Parede(335+230,145+430, 20,50)]
            self.paredes_direita = [Parede(335+540,145+10, 20,350), Parede(335+120,145+70, 20,170),Parede(335+360,145+70, 20,170),
                                    Parede(335+120,145+310, 20,110), Parede(335+600,145+370, 20,110)]   
            
            self.objetivos = [Objetivo(335+250,145+430, 50,50), Objetivo(335+310,145+430, 50,50), Objetivo(335+370,145+430, 50,50)]
        
        if fase == 3:
            self.mapa = pygame.image.load('puzzle1/grapichs_puzzle2/fase_3.png')
            self.fase = 3
            self.resolucao = (360,115)
            self.escala_movimento = 0.5
            self.personagem = Personagem(360+190,145+370, 120, 0.5)
            self.moveis = [Movel(360 + 190, 145 + 250, pygame.image.load('puzzle1/grapichs_puzzle2/maca_hospital.png'), 60, 1),
                           Movel(360 + 190, 145 + 130, pygame.image.load(
                               'puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 1),
                           Movel(360 + 370, 145 + 250, pygame.image.load(
                               'puzzle1/grapichs_puzzle2/aparelho_hospital.png'), 60, 1)]
            
            self.paredes_cima = [Parede(360+70,145-10, 170,20), Parede(360+370,145+110, 170,20), Parede(360+10,145+170, 50,20),
                                 Parede(360+250,145+230, 110,20)]
            self.paredes_baixo = [Parede(360+250,145+300, 290,20), Parede(360+10,145+360, 50,20), Parede(360+70,145+420, 170,20)]
            self.paredes_esquerda = [Parede(360+50,145+10, 20,170),Parede(360+350,145+130, 20,110),Parede(360-10,145+190, 20,170),
                                     Parede(360+50,145+370, 20,50)]
            self.paredes_direita = [Parede(360+240,145+10, 20,230), Parede(360+540,145+130, 20,170),Parede(360+240,145+310, 20,110)]   
            
            self.objetivos = [Objetivo(360+10,145+190, 50,50), Objetivo(360+10,145+250, 50,50), Objetivo(360+10,145+310, 50,50)]

        if fase == 4:
            self.fase = 4
            comecar_coleta()

    def loop(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if (evento.type == pygame.KEYDOWN)and(not self.animação):
                    if (evento.key == pygame.K_d)and self.podeandar(self.personagem, 'direita', 'não'):
                        self.personagem.movimento('direita', self.escala_movimento)
                        if(self.personagem.passos<90):    
                            self.animação = True
                            self.animaçãodireita = True
                        else:
                            self.animação = False
                            self.animaçãodireita = False
                            self.personagem.passos = 0
                    if (evento.key == pygame.K_a)and self.podeandar(self.personagem, 'esquerda', 'não'):
                        self.personagem.movimento('esquerda', self.escala_movimento)
                        if(self.personagem.passos<90):    
                            self.animação = True
                            self.animaçãoesquerda = True
                        else:
                            self.animação = False
                            self.animaçãoesquerda = False
                            self.personagem.passos = 0
                    if (evento.key == pygame.K_s)and self.podeandar(self.personagem, 'baixo', 'não'):
                        self.personagem.movimento('baixo', self.escala_movimento)
                        if(self.personagem.passos<90):    
                            self.animação = True
                            self.animaçãobaixo = True
                        else:
                            self.animação = False
                            self.animaçãobaixo = False
                            self.personagem.passos = 0
                    if (evento.key == pygame.K_w)and self.podeandar(self.personagem, 'cima', 'não'):
                        self.personagem.movimento('cima', self.escala_movimento)
                        if(self.personagem.passos<90):    
                            self.animação = True
                            self.animaçãocima = True
                        else:
                            self.animação = False
                            self.animaçãocima = False
                            self.personagem.passos = 0
            if self.fase == 4:
                self.tela.fill((18,18,18))
                self.tela.blit(self.text_surf, (480,350))

            else:                  
                if (self.animação):
                    if (self.animaçãodireita) :
                        self.personagem.movimento('direita', self.escala_movimento)
                        if(self.personagem.passos<31):    
                            self.animação = True
                            self.animaçãodireita = True
                        else:
                            self.animação = False
                            self.animaçãodireita = False
                            self.personagem.passos = 0
                    if (self.animaçãoesquerda) :
                        self.personagem.movimento('esquerda', self.escala_movimento)
                        if(self.personagem.passos<31):    
                            self.animação = True
                            self.animaçãoesquerda = True
                        else:
                            self.animação = False
                            self.animaçãoesquerda = False
                            self.personagem.passos = 0
                    if (self.animaçãobaixo) :
                        self.personagem.movimento('baixo', self.escala_movimento)
                        if(self.personagem.passos<31):    
                            self.animação = True
                            self.animaçãobaixo = True
                        else:
                            self.animação = False
                            self.animaçãobaixo = False
                            self.personagem.passos = 0
                    if (self.animaçãocima) :
                        self.personagem.movimento('cima', self.escala_movimento)
                        if(self.personagem.passos<31):    
                            self.animação = True
                            self.animaçãocima = True
                        else:
                            self.animação = False
                            self.animaçãocima = False
                            self.personagem.passos = 0


                
                keys = pygame.key.get_pressed()
                self.tela.fill((18,18,18))
                self.tela.blit(self.mapa, self.resolucao)

                self.colisao_moveis()
                
                

                self.personagem.desenhar_personagem(self.tela)
                for movel in self.moveis:
                    movel.desenhar_movel(self.tela)
                    movel.reset_movimento()
                self.personagem.reset_movimento()
                self.tela.blit(self.text_surf, (35, 60))
                
                if self.fase == 1:
                    if keys[pygame.K_r] and self.personagem.passos == 0 and self.contagem == 0:
                        self.personagem = Personagem(590,190, 120, 1)
                        self.moveis = [Movel(470, 310, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 2),
                                       Movel(710, 310, pygame.image.load(
                                           'puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 2)]
                            
                    if self.moveis[0].rect.colliderect(self.objetivos[0]) and self.moveis[1].rect.colliderect(self.objetivos[1]) and self.personagem.passos == 0 and self.contagem == 0:
                        self.som_acerto.play()
                        self.mudar_fase(2)
                    #self.mudar_fase(2)
                if self.fase == 2:
                    if keys[pygame.K_r] and self.personagem.passos == 0 and self.contagem == 0:
                        self.personagem = Personagem(525,395, 60, 0.5)
                        self.moveis = [Movel(585, 395, pygame.image.load('puzzle1/grapichs_puzzle2/maca_hospital.png'), 60, 1),
                                       Movel(405, 275, pygame.image.load(
                                           'puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 1),
                                       Movel(825, 215, pygame.image.load(
                                           'puzzle1/grapichs_puzzle2/aparelho_hospital.png'), 60, 1)]

                    if self.moveis[0].rect.colliderect(self.objetivos[1]) and self.moveis[1].rect.colliderect(self.objetivos[2]) and self.moveis[2].rect.colliderect(self.objetivos[0]) and self.personagem.passos == 0 and self.contagem == 0:
                        self.som_acerto.play()
                        self.mudar_fase(3)
                
                if self.fase == 3:
                    if keys[pygame.K_r] and self.personagem.passos == 0 and self.contagem == 0:
                        self.personagem = Personagem(360+190,145+370, 60, 0.5)
                        self.moveis = [Movel(360 + 190, 145 + 250, pygame.image.load(
                            'puzzle1/grapichs_puzzle2/maca_hospital.png'), 60, 1),
                                       Movel(360 + 190, 145 + 130, pygame.image.load(
                                           'puzzle1/grapichs_puzzle2/armario_hospital.png'), 60, 1),
                                       Movel(360 + 370, 145 + 250, pygame.image.load(
                                           'puzzle1/grapichs_puzzle2/aparelho_hospital.png'), 60, 1)]
                    if self.objetivos[0].rect.collidelist(self.moveis) != -1 and self.objetivos[1].rect.collidelist(self.moveis) != -1 and self.objetivos[2].rect.collidelist(self.moveis) != -1 and self.personagem.passos == 0 and self.contagem == 0:
                        self.som_acerto.play()
                        self.mudar_fase(4)

            # Exibe as informações dos coletáveis:
            def visualizar_infos_coletaveis():
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
            visualizar_infos_coletaveis()
            pygame.display.flip()
            self.clock.tick(60)

def comecar_desafio_puzzle2():
    puzzle = Puzzle_2()
    puzzle.loop()