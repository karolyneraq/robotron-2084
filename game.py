import pygame

from config import *
from layouts import Layouts
from player import Player
from human import Human

pygame.joystick.init()
Joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()

        # Player
        self.player = Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        # Humans
        self.mother = Human("Mother", (500, 200))
        self.father = Human("Father", (100, 100))
        self.baby = Human("Baby", (400, 500))

        self.human_group = pygame.sprite.Group()
        self.human_group.add(self.mother)
        self.human_group.add(self.father)
        self.human_group.add(self.baby)

        self.wave = 0
        self.font = pygame.font.Font('robotron-2084.ttf', 25)

    # Check if an event happens
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if len(Joysticks) == 0:
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.player.set_movement_keys(event)
                    self.player.set_fire_keys(event)
            else:
                if event.type == pygame.JOYAXISMOTION:
                    self.player.set_movement()
                    self.player.set_fire()

    # sets the game looping
    def game_loop(self):

        while self.loop:
            self.screen.blit(game_surface, (proportion / 2, proportion / 2))
            self.draw_sprites()
            self.check_events()

            # Player
            self.player.set_obstacles(self.walls)
            self.player_group.update()

            for bullet in self.player.get_bullets():
                bullet.move()

            for bullet in self.player.get_bullets():
                bullet.move()
            self.player_group.draw(self.screen)
            self.player.get_bullets().draw(self.screen)
            self.player_group.update()

            # Humans
            self.mother.set_obstacles(self.walls)
            self.father.set_obstacles(self.walls)
            self.baby.set_obstacles(self.walls)
            self.human_group.update()

            # Score Display
            score = f'{self.player.get_score():04d}'
            score_txt = self.font.render(score, True, white)
            self.screen.blit(score_txt, (200, 10))

            # Wave Display
            wave = f'{self.wave}'
            wave_number = self.font.render(wave, True, white)
            self.screen.blit(wave_number, (450, 610))

            wave_txt = self.font.render("WAVE", True, white)
            self.screen.blit(wave_txt, (510, 610))

            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player_group.draw(self.screen)
        self.player.get_bullets().draw(self.screen)
        self.human_group.draw(self.screen)
