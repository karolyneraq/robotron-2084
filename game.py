from random import randint
from config import *
from player import Player
from enemys import Enemy
import pygame


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.enemy_group = pygame.sprite.Group()
        self.player = Player("player_img_front", WIDTH // 2, HEIGHT // 2, player_height, player_width)
        self.bullet_group = pygame.sprite.Group()
        self.run = True
        self.menu = False
        self.clock = pygame.time.Clock()

        for cnt in range(randint(1, 10)):
            enemy = Enemy("enemy_img.png", randint(0, WIDTH), randint(50, HEIGHT))
            self.enemy_group.add(enemy)

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, (255, 0, 0), (0, 50, WIDTH, HEIGHT - 50), 5)
        self.bullet_group.draw(self.screen)
        self.player.draw(self.screen)
        for curr_enemy in self.enemy_group:
            curr_enemy.draw(self.screen)
        pygame.display.update()

    def run_menu(self, menu):
        while menu:
            self.screen.fill(BLACK)
            self.screen.blit(play_img, (WIDTH // 2, (HEIGHT - 50) // 2))

    def main_loop(self):
        while not self.menu:
            while self.run:
                self.clock.tick(FPS)
                self.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.bullet_group.add(self.player.create_bullet())

                        for curr_bullet in self.bullet_group:
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_w]:
                                curr_bullet.move_y(up=True)
                            if keys[pygame.K_s]:
                                curr_bullet.move_y(up=False)
                            if keys[pygame.K_d]:
                                curr_bullet.move_x(right=True)
                            if keys[pygame.K_a]:
                                curr_bullet.move_x(right=False)
                gets_hit = pygame.sprite.spritecollideany(self.player, self.enemy_group)
                print(gets_hit)
                keys = pygame.key.get_pressed()
                self.player.player_movement(keys, self.player, self.bullet_group)
                self.player.player_rotation(keys, self.player, self.screen, self.player.x, self.player.y)
                Enemy.enemy_movement(self.enemy_group, self.player)
                self.bullet_group.update()
            pygame.quit()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.main_loop()
    