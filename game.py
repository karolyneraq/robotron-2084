import random
from config import *
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
        self.player = Player((500, 300), player)
        self.player_sprites.add(self.player)
        self.background = game_surface


    # Check if an event happens
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def bullet_collision(self):
        for bullet in self.player.bullet_list:
            for wall in self.walls:
                if wall.collide_mask(bullet.rect):
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

            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player_sprites.draw(self.screen)
        self.player.bullet_group.draw(self.screen)
        self.player.bullet_group.update()   
