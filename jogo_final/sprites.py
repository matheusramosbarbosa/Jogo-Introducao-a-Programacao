from configuracoes import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = WORLD_LAYERS['principal']):
        super().__init__(groups) # Inicializa o sprite
        self.image = surf # Define a imagem do sprite
        self.rect = self.image.get_frect(topleft = pos) # Define a posição do retângulo da imagem
        self.z = z
        self.y_sort = self.rect.centery
        self.hitbox = self.rect.copy()

class SpriteOpacidade(Sprite):
    def __init__(self, pos, surf, groups,):
        super().__init__(pos, surf, groups)

class BorderSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()

class CollidableSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.inflate(-30, -self.rect.height * 0.9)

class PlantinhasSprite(Sprite):
    def __init__(self, pos, surf, groups, z = WORLD_LAYERS['principal']):
        super().__init__(pos, surf, groups, z)
        self.y_sort = self.rect.centery - 20
       
class SpriteTransicao(Sprite):
    def __init__(self, pos, size, target, groups):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.target = target

class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups, z = WORLD_LAYERS['principal']):
        self.frame_index, self.frames = 0, frames
        super().__init__(pos, frames[self.frame_index], groups, z)

    def animate(self, dt):
        self.frame_index += 4 * dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]

    def update(self, dt):
        self.animate(dt)