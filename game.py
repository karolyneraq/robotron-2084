from random import randint
from config import *
from enemy import Enemy
from player import Player
from layouts import Layouts

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player_sprites = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.player = Player((500, 300), player)
        self.player_sprites.add(self.player)
        self.background = game_surface
        for i in range(randint(1, 10)):
            enemy = Enemy(randint(0, screen_width), randint(50, screen_height), self.player)
            self.enemy_group.add(enemy)

    # Check if an event happens
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.player.shoot()

    def bullet_collision(self):
        # sets the collision between bullet and wall groups
        for wall in self.walls:
            for bullet in self.player.bullet_group:
                if pygame.sprite.collide_mask(bullet, wall):
                    bullet.kill()
        # clear the ball list
        self.player.bullet_list.clear()

    def player_collision(self):
        for wall in self.walls:
            if pygame.sprite.collide_mask(self.player, wall):
                if abs(self.player.rect.top - wall.rect.bottom) < 60:
                    self.player.rect.y += player_speed
                elif abs(wall.rect.top - self.player.rect.bottom) < 40:
                    self.player.rect.y -= player_speed
                elif abs(wall.rect.left - self.player.rect.right) < 74:
                    self.player.rect.x -= player_speed
                elif abs(self.player.rect.left - wall.rect.right) < 74:
                    self.player.rect.x += player_speed

    # sets the game looping
    def game_loop(self):

        while self.loop:
            self.screen.blit(game_surface, (0, 0))
            self.check_events()
            self.draw_sprites()
            self.player.move()
            self.player_collision()
            self.bullet_collision()
            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player.update()
        self.player_sprites.draw(self.screen)
        self.player.bullet_group.draw(self.screen)
        self.player.bullet_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()