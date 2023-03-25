import pygame

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robotron")
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# sizes
player_width = 22
player_height = 32
width28 = 28
height36 = 36
no_34 = 34

# Images
player_img_front = pygame.transform.scale(pygame.image.load('assets/player_front.png'), (22, 32))
player_img_left = pygame.transform.scale(pygame.image.load('assets/player_left.png'), (22, 32))
player_img_right = pygame.transform.scale(pygame.image.load('assets/player_right.png'), (22, 32))
player_img_back = pygame.transform.scale(pygame.image.load('assets/player_back.png'), (22, 32))
enemy_img = pygame.transform.scale(pygame.image.load('assets/enemy_img.png'), (32, 32))
play_img = pygame.image.load('assets/play.png')

# Hit boxes
# player_rect = pygame.draw.rect(win, (0, 0, 255,), player.hit_box, 2)
# enemy_rect = pygame.draw.rect(win, (255, 0, 0), enemy.hit_box, 2)
