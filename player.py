from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        