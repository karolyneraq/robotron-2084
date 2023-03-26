import pygame

from config import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player_positions):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_vel = 2
        self.hit_box = (self.x, self.y, 34, 34)
        self.assets = []
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Vermelho/left_feet_raised.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Vermelho/right_feet_raised.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.current_sprite = 0
        self.image = self.assets[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.moving_x = False
        self.moving_y = False
        self.player = player_positions

    def move_x(self, right=True):
        if right:
            self.rect.x += self.enemy_vel
        else:
            self.rect.x -= self.enemy_vel
        self.moving_x = True

    def move_y(self, above=True):
        if above:
            self.rect.y += self.enemy_vel
        else:
            self.rect.y -= self.enemy_vel
        self.moving_y = True
        # self.image = self.assets[self.current_sprite]

    def enemy_movement(self):
        self.moving_x = False
        self.moving_y = False

        if self.player.y >= self.rect.y - 30:
            self.move_y(above=True)
        if self.player.y <= self.rect.y:
            self.move_y(above=False)
        if self.player.x >= self.rect.x - 60:
            self.move_x(right=True)
        if self.player.x <= self.rect.x - 50:
            self.move_x(right=False)

        if self.current_sprite >= 4:
            self.current_sprite = 0
        else:
            self.current_sprite += 0.05

        self.image = self.assets[int(self.current_sprite)]

    def update(self):
        self.enemy_movement()