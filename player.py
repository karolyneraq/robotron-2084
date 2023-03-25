from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, pos, current_sprite):
        super().__init__()
        self.score = 0
        self.bullet_group = pygame.sprite.Group()
        self.img_player = []
        for i in range(4):
            for j in range(4):
                self.img_player.append(sheet.subsurface((j*6, i*10), (6, 10)))
        self.direction = current_sprite
        self.image = self.img_player[self.direction]
        self.image = pygame.transform.scale(sheet, (90, 135))
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.x = pos[0]
        self.y = pos[1]

