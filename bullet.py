from config import *


def bullet_movement_1(keys, bullet_group):
    for curr_bullet in bullet_group:
        if keys[pygame.K_w]:
            curr_bullet.move_y(up=True)
        if keys[pygame.K_s]:
            curr_bullet.move_y(up=False)
        if keys[pygame.K_d]:
            curr_bullet.move_x(right=True)
        if keys[pygame.K_a]:
            curr_bullet.move_x(right=False)


def bullet_movement(bullet):
    bullet.rect.x += bullet_vel


class Bullet(pygame.sprite.Sprite):
    bullet_vel = 5

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def move_x(self, right=True):
        if right:
            self.rect.x += self.bullet_vel
        else:
            self.rect.x -= self.bullet_vel

    def move_y(self, up=True):
        if up:
            self.rect.y -= self.bullet_vel
        else:
            self.rect.y += self.bullet_vel

    def update(self):
        if self.rect.x >= WIDTH + 3 or self.rect.x <= -3:
            self.kill()

        elif self.rect.y >= HEIGHT + 3 or self.rect.y <= -3:
            self.kill()

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
