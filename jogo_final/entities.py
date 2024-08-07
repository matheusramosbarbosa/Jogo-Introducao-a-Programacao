from configuracoes import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)
        self.z = WORLD_LAYERS['principal']

        # movimentacao
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 250
        self.blocked = False

        # graficos
        self.frame_index, self.frames = 0, frames
        self.facing_direction = 'down'

        # config do sprite
        self.image = self.frames[self.get_state()][self.frame_index]
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-self.rect.width // 2, -60)
        self.y_sort = self.rect.centery

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[self.get_state()][int(self.frame_index % len(self.frames[self.get_state()]))]

    def get_state(self):
        moving = bool(self.direction.length())
        if moving:
            if self.direction.x != 0:
                self.facing_direction = 'right' if self.direction.x > 0 else 'left'
            if self.direction.y != 0:
                self.facing_direction = 'down' if self.direction.y > 0 else 'up'
        return f'{self.facing_direction}{'' if moving else "_idle"}'
    
    def bloquear_movimento(self):
        self.blocked = True
        self.direction = vector(0, 0)
    
    def unblock(self):
        self.blocked = False
    
class Character(Entity):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)

class Player(Entity):
    def __init__(self, pos, frames, groups, sprites_colisoes):
        super().__init__(pos, frames, groups)
        self.sprites_colisoes = sprites_colisoes
        self.movimento = False
        self.moving_direction= 'frente'

    def mover(self):
        tecla = pygame.key.get_pressed()
        self.movimento = False
        self.direction.update(0, 0)  # Reinicia a direção a cada chamada

        if tecla[pygame.K_a]:
            self.direction.x = -1
            self.moving_direction = 'esquerda'
            self.movimento = True

        if tecla[pygame.K_d]:
            self.direction.x += 1
            self.moving_direction = 'direita'
            self.movimento = True

        if tecla[pygame.K_w]:
            self.direction.y = -1
            self.moving_direction = 'costas'
            self.movimento = True

        if tecla[pygame.K_s]:
            self.direction.y += 1
            self.moving_direction = 'frente'
            self.movimento = True

    # def input(self):
    #     keys = pygame.key.get_pressed()
    #     input_vector = vector()
    #     if keys[pygame.K_UP]:
    #         input_vector.y -= 1
    #     if keys[pygame.K_DOWN]:
    #         input_vector.y += 1
    #     if keys[pygame.K_LEFT]:
    #         input_vector.x -= 1
    #     if keys[pygame.K_RIGHT]:
    #         input_vector.x += 1
    #     self.direction = input_vector


    def move(self, dt):
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        self.rect.centerx += self.direction.x * self.speed * dt
        self.hitbox.centerx = self.rect.centerx
        self.colisoes('horizontal')

        self.rect.centery += self.direction.y * self.speed * dt
        self.hitbox.centery = self.rect.centery
        self.colisoes('vertical')

    def colisoes(self, axis):
        for sprite in self.sprites_colisoes:
            if sprite.hitbox.colliderect(self.hitbox):
                if axis == 'horizontal':
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                    self.rect.centerx = self.hitbox.centerx  # Atualiza o rect apenas após a colisão

                elif axis == 'vertical':
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                    self.rect.centery = self.hitbox.centery  # Atualiza o rect apenas após a colisão
                
                # correção do hitbox depois de colidir

                while sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.top -= 1
                    elif self.direction.y < 0:
                        self.hitbox.bottom += 1
                    self.rect.centery = self.hitbox.centery


    def update(self, dt):
        self.y_sort = self.rect.centery
        if not self.blocked:
            self.mover()
            self.move(dt)
            self.animate(dt)