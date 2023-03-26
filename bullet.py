from config import *
from layouts import Layouts


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = bullet_speed
        self.image = pygame.transform.scale(bullet, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.walls = Layouts().get_group()

    def update(self):
        self.rect.x += (self.direction * self.speed)
        self.rect.y += (self.direction * self.speed)
        for wall in self.walls:
            if pygame.sprite.collide_mask(wall, self.image):
                self.kill()



        
            
        