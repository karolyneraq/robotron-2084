import wall
from config import *


# layouts class 
class Layouts:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.wall_color = yellow
        self.borders()

    def get_group(self):
        return self.group
    
    def borders(self):
        self.group.add(wall.Wall(self.wall_color, (910, 5), (45, 45)))
        self.group.add(wall.Wall(self.wall_color, (910, 5), (45, 600)))
        self.group.add(wall.Wall(self.wall_color, (5, 555), (45, 45)))
        self.group.add(wall.Wall(self.wall_color, (5, 555), (950, 45)))
    