from config import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_vel = 3
        self.hit_box = (self.x, self.y, 34, 34)
        self.assets = []
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.current = 0
        self.image = self.assets[0]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def move_x(self, right=True):
        if right:
            self.x += self.enemy_vel
        else:
            self.x -= self.enemy_vel

    def move_y(self, above=True):
        if above:
            self.y += self.enemy_vel
        else:
            self.y -= self.enemy_vel

    def draw(self, win):
        self.hit_box = (self.x, self.y, 34, 34)
        # pygame.draw.rect(win, (0,255,0), self.hit_box, 2)
        win.blit(self.image, (self.x, self.y))

    @staticmethod
    def enemy_movement(enemy_group, player):
        for curr_enemy in enemy_group:
            if player.y >= curr_enemy.y - 30:
                curr_enemy.move_y(above=True)
            if player.y <= curr_enemy.y:
                curr_enemy.move_y(above=False)
            if player.x >= curr_enemy.x - 60:
                curr_enemy.move_x(right=True)
            if player.x <= curr_enemy.x - 50:
                curr_enemy.move_x(right=False)
