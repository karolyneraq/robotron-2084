from game import Game
from config import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robotron")

play = Game(screen)
Game.game_loop(play)
