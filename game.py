from config import *
from layouts import Layouts
from player import Player

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player = Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

    # Check if an event happens
    def check_events(self):
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
            self.draw_sprites()

            self.check_events()
            self.player.set_obstacles(self.walls)
            self.player_group.update()

            for bullet in self.player.get_bullets():
                bullet.move()

            for bullet in self.player.get_bullets():
                bullet.move()
            self.player_group.draw(self.screen)
            self.player.get_bullets().draw(self.screen)
            self.player_group.update()

            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player_group.draw(self.screen)
        self.player.get_bullets().draw(self.screen)
