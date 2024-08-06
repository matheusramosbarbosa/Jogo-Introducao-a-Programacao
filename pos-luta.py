import pygame
pygame.init()
tela = pygame.display.set_mode((1280, 720))
todos_sprites = pygame.sprite.Group()
relogio = pygame.time.Clock()
tempo = relogio.tick()
pygame.mixer.music.load('toby fox - UNDERTALE Soundtrack - 31 Waterfall.mp3')
pygame.mixer.music.play(-1)
class Cenario(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'boss-area-cac.png')
        self.rect = self.image.get_rect(center=(640, 360))
cenario = Cenario(todos_sprites)
todos_sprites.update(tempo)
todos_sprites.draw(tela)
pygame.display.update()

class Personagem:
    # Define a função de incialização do objeto Personagem:
    def __init__(self, x, y):
        self.x = y - 200
        self.y = y + 80
        self.direcao = 'esquerda'
        self.passo = 0
        self.contador_passos = 0
        self.movimento = False

    # Função para desenhar o personagem:
    def desenhar(self, tela, moveu, x , y, passo):
        if passo > 0 and passo % 2 == 0:
            passo = 0
        else:
            passo = 1
        self.imagens = [pygame.image.load('prota-esquerda-1.png'), pygame.image.load('prota-esquerda-2.png')]
        self.imagens_parado = pygame.image.load('prota-esquerda-0.png')
        if moveu:
            tela.blit(self.imagens[passo], (x, y))
        else:
            tela.blit(self.imagens_parado, (x, y))
x = 420
y = 330
passos = 0
Personagem.desenhar(Personagem, tela, False, x, y, passos)
pygame.display.update()
for i in range(3):
    class Boss(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load(f'boss-morre-{i}.png')
            self.rect = self.image.get_rect(center=(240, 340))
    boss = Boss(todos_sprites)
    todos_sprites.update(tempo)
    todos_sprites.draw(tela)
    Personagem.desenhar(Personagem, tela, False, x, y, passos)
    pygame.display.update()
    pygame.time.wait(350)
    boss.remove(todos_sprites)
class Cracha(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'cracha-drop.png')
        self.rect = self.image.get_rect(center=(240, 390))

cracha = Cracha(todos_sprites)
todos_sprites.update(tempo)
todos_sprites.draw(tela)
pygame.display.update()
cracha_dropado = True
moveu = False

todos_sprites.update(tempo)
todos_sprites.draw(tela)
Personagem.desenhar(Personagem, tela, False, x, y, passos)
pygame.display.update()
while cracha_dropado:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 20
                passos += 1
                if x < 235:
                    cracha_dropado = False
                    cracha.remove(todos_sprites)
                    item = pygame.mixer.Sound('item get 1.wav')
                    item.play()
                    todos_sprites.update(tempo)
                    todos_sprites.draw(tela)
                    Personagem.desenhar(Personagem, tela, True, x, y, passos)
                    pygame.display.update()
                    pygame.time.wait(1000)
                else:
                    todos_sprites.update(tempo)
                    todos_sprites.draw(tela)
                    Personagem.desenhar(Personagem, tela, True, x, y, passos)
                    pygame.display.update()