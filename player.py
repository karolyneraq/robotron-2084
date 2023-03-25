from config import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y, height, width):
        super().__init__()
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.width = player_width
        self.height = player_height
        self.hit_box = (self.x - 2, self.y - 2, 28, 36)
        self.image = player_img_front
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.player_vel = 7
        self.player_width = 1
        self.player_height = 1

    def move_x(self, right=True):
        if right:
            self.x -= self.player_vel
        else:
            self.x += self.player_vel

    def move_y(self, up=True):
        if up:
            self.y -= self.player_vel
        else:
            self.y += self.player_vel

    def draw(self, win):
        self.hit_box = (self.x - 2, self.y - 2, 28, 36)
        # pygame.draw.rect(win, (255,0,0), self.hit_box,2)
        win.blit(player_img_front, (self.x, self.y))

    def create_bullet(self):
        return Bullet(self.x, self.y)

    @staticmethod
    def player_rotation(keys, player, win, x, y):
        if keys[pygame.K_w]:
            win.blit(player_img_back, (x, y))
        if keys[pygame.K_s]:
            win.blit(player_img_front, (x, y))
        if keys[pygame.K_d]:
            win.blit(player_img_right, (x, y))
        if keys[pygame.K_a]:
            win.blit(player_img_left, (x, y))
        pygame.display.update()

    @staticmethod
    def player_movement(keys, player, bullet):
        if keys[pygame.K_w] and player.y - player.player_vel - 1 > 53:
            player.move_y(up=True)
        if keys[pygame.K_s] and player.y + player.player_vel + 32 + 1 <= HEIGHT:
            player.move_y(up=False)

        if keys[pygame.K_a] and player.x - player.player_vel - 1 >= 0:
            player.move_x(right=True)

        if keys[pygame.K_d] and player.x + player.player_vel + 32 - 8 <= WIDTH:
            player.move_x(right=False)
