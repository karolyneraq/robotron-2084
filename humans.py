import random
from config import *


class Humans(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.human_vel = 1
        # self.hit_box = (self.x, self.y, 34, 34)
        self.assets = []
        self.assets.append(pygame.transform.scale(pygame.image.load('Assets/Baby.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('Assets/Mother.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('Assets/Father.png'), (32, 42)))
        self.current_sprite = random.randint(0, 2)
        self.image = self.assets[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.moving_x = False
        self.moving_y = False
        self.flip = False

    def human_movement(self, collide):
        if collide:
            self.flip = not self.flip
            self.human_vel = -self.human_vel

        else:
            self.rect.x += self.human_vel
        self.image = self.assets[int(self.current_sprite)]

    def update(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        collide = False
        self.human_movement(collide)
