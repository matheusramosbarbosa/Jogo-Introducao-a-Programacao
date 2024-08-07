import pygame

def exibir_final():
    pygame.init()
    tela = pygame.display.set_mode((1280,720))
    todos_sprites = pygame.sprite.Group()
    class Lucas(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/lucas-frente-com0.png')
            self.rect = self.image.get_rect(center=(640,360))

    lucas = Lucas(todos_sprites)
    class Dialogo1(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/obrigado.png')
            self.rect = self.image.get_rect(center=(640, 605))
    dialogo1 = Dialogo1(todos_sprites)
    tela.fill('black')
    todos_sprites.update()
    todos_sprites.draw(tela)
    pygame.display.update()
    pygame.time.wait(5000)
    dialogo1.remove(todos_sprites)
    class Dialogo2(pygame.sprite.Sprite):
        def __init__(self, groups):
            super().__init__(groups)
            self.image = pygame.image.load('puzzle1/imagens-batalha/por-conta.png')
            self.rect = self.image.get_rect(center=(640, 605))

    dialogo2 = Dialogo2(todos_sprites)
    tela.fill('black')
    todos_sprites.update()
    todos_sprites.draw(tela)
    pygame.display.update()
    pygame.time.wait(5000)
    dialogo2.remove(todos_sprites)