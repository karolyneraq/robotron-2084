from config import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.score = 0
        self.bullet_list = []
        self.bullet_group = pygame.sprite.Group()
        self.image = sprite
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.x = pos[0]
        self.y = pos[1]
        self.direction_player = 1

    def move(self):
        # sets the movement keys to get pressed
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rect.x += -self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_w]:
            self.rect.y += -self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed

        self.x = self.rect.x
        self.y = self.rect.y

    def shoot(self):
        bullet = Bullet(self.rect.centerx + (0.2 * self.rect.size[0]*self.direction_player),
                            self.rect.centery, self.direction_player)
        self.bullet_group.add(bullet)
        self.bullet_list.append(bullet)
