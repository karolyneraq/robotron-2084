import random
from config import *
from player import Player
from layouts import Layouts

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player_sprites = pygame.sprite.Group()
        self.player_sprites.add(Player(player_sheet, (500, 300), random.randrange(0, 12, 4)))

    # Check if an event happens
    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # sets the game looping
    def game_loop(self):

        while self.loop:
            self.screen.blit(game_surface, (proportion / 2, proportion / 2))
            self.draw_sprites()

            self.check_events() 

            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player_sprites.draw(self.screen)
        self.player_sprites.update()        
