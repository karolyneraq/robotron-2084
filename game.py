from random import randint
from config import *
from player import Player
from layouts import Layouts
from enemy import Enemy

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player_sprites = pygame.sprite.Group()
        self.player = Player((500, 300), player)
        self.player_sprites.add(self.player)
        self.background = game_surface
        self.enemy_group = pygame.sprite.Group()

        for cnt in range(randint(1, 10)):
            enemy = Enemy(randint(0, screen_width), randint(50, screen_height), self.player)
            self.enemy_group.add(enemy)

    # Check if an event happens
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def bullet_collision(self, bullet):
        for wall in self.walls:
            if pygame.sprite.collide_mask(bullet, wall):
                bullet.kill()

    # sets the game looping
    def game_loop(self):

        while self.loop:
            self.screen.blit(game_surface, (0, 0))
            self.check_events()
            self.draw_sprites()

            for bullet in self.player.bullet_list:
                self.bullet_collision(bullet)

            self.enemy_group.update()

            self.player.move()

            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player_sprites.draw(self.screen)
        self.player.bullet_group.draw(self.screen)
        self.player.bullet_group.update()
        self.enemy_group.draw(self.screen)

        pygame.display.update()
