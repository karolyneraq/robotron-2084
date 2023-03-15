import pygame
from config import *
from player import Player


# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.player = Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

    # Check if an event happens
    def check_events(self):
        clk.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.player.set_movement_keys(event)
                self.player.set_fire_keys(event)

    # sets the game looping
    def game_loop(self):

        while self.loop:
            self.screen.blit(game_surface, (proportion / 2, proportion / 2))
            self.draw_borders()
            self.check_events()

            for bullet in self.player.get_bullets():
                bullet.move()
            self.player_group.draw(self.screen)
            self.player.get_bullets().draw(self.screen)
            self.player_group.update()

            pygame.display.update()
            clk.tick(fps)

    def draw_borders(self):
        pygame.draw.rect(self.screen, yellow, (proportion / 2 - border_width, proportion / 2 - border_width,
                                               screen_width - proportion + (border_width * 2), border_width))

        pygame.draw.rect(self.screen, yellow, (proportion / 2 - border_width, screen_height - (proportion / 2),
                                               screen_width - proportion + (border_width * 2), border_width))

        pygame.draw.rect(self.screen, yellow, ((proportion / 2) - border_width, (proportion / 2) - border_width,
                                               border_width, screen_height - proportion + border_width))

        pygame.draw.rect(self.screen, yellow, (screen_width - (proportion / 2), (proportion / 2) - border_width,
                                               border_width, screen_height - proportion + border_width))
