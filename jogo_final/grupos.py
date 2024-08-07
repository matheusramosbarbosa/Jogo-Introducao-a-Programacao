from configuracoes import *

class TodosSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector(100,20)

    def draw(self, player_center):
        self.offset.x = -(player_center[0] - WINDOW_WIDTH // 2)
        self.offset.y = -(player_center[1] - WINDOW_HEIGHT // 2)

        fundo_sprites = [sprite for sprite in self if sprite.z < WORLD_LAYERS['principal']]

        principal_sprites = sorted([sprite for sprite in self if sprite.z == WORLD_LAYERS['principal']], key = lambda sprite: sprite.y_sort)

        cima_sprites = [sprite for sprite in self if sprite.z > WORLD_LAYERS['principal']]

        for camada in (fundo_sprites, principal_sprites, cima_sprites):
            for sprite in camada:
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)