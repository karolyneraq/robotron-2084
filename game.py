import pygame
from config import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robotron")

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()

game_surface = pygame.Surface((screen_width - proportion, screen_height - proportion))


def draw_borders():
    global screen
    pygame.draw.rect(screen, yellow, (proportion / 2 - border_width, proportion / 2 - border_width,
                                      screen_width-proportion + (border_width*2), border_width))

    pygame.draw.rect(screen, yellow, (proportion / 2 - border_width, screen_height - (proportion/2),
                                      screen_width - proportion + (border_width * 2), border_width))

    pygame.draw.rect(screen, yellow, ((proportion/2) - border_width, (proportion/2) - border_width,
                                      border_width, screen_height - proportion + border_width))

    pygame.draw.rect(screen, yellow, (screen_width - (proportion / 2), (proportion / 2) - border_width,
                                      border_width, screen_height - proportion + border_width))


class Game:
    def __init__(self):
        pass

    # Check if an event happens
    @staticmethod
    def check_events():
        clk.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def game_loop(self):

        while True:
            screen.blit(game_surface, (proportion / 2, proportion / 2))
            draw_borders()

            self.check_events()
            pygame.display.update()

            clk.tick(fps)
