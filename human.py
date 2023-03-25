import pygame
from config import *
import random


class Human(pygame.sprite.Sprite):
    def __init__(self, person, spawn):
        super().__init__()
        path = "assets/"
        self.sprites = []
        self.speed_x = 1
        self.speed_y = 1
        self.directions = ["up", "down", "left", "right"]

        if person == "Mother":
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "Mother.png"), (shape_ppt, shape_ppt)))

        elif person == "Father":
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "Father.png"), (shape_ppt, shape_ppt)))

        elif person == "Baby":
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "Baby.png"), (shape_ppt, shape_ppt)))

        self.image = self.sprites[0]
        self.rect = self.image.get_rect(topleft=spawn)
        self.obstacles = None

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles

    def update(self):
        self.move()

    def move(self):
        self.rect.x = self.rect.x + self.speed_x
        self.collision()
        self.rect.y = self.rect.y + self.speed_y
        self.collision()

    def collision(self):
        collision_tolerance = 10
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect):
                if abs(self.rect.top - sprite.rect.bottom) < collision_tolerance and self.speed_y < 0:
                    self.speed_y *= -1
                if abs(self.rect.bottom - sprite.rect.top) < collision_tolerance and self.speed_y > 0:
                    self.speed_y *= -1
                if abs(self.rect.right - sprite.rect.left) < collision_tolerance and self.speed_x > 0:
                    self.speed_x *= -1
                if abs(self.rect.left - sprite.rect.right) < collision_tolerance and self.speed_x < 0:
                    self.speed_x *= -1
        if self.rect.x >= 850 and self.speed_x > 0:
            self.speed_x *= -1
        elif self.rect.x <= 0 and self.speed_x < 0:
            self.speed_x *= -1
        if self.rect.y >= 600 and self.speed_y > 0:
            self.speed_y *= -1
        elif self.rect.y <= 0 and self.speed_y < 0:
            self.speed_y *= -1