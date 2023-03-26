from random import *
from config import *
from enemy import Enemy
from player import Player
from layouts import Layouts
from humans import Humans

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player_sprites = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.human_group = pygame.sprite.Group()
        self.player = Player((500, 300), player)
        self.player_sprites.add(self.player)
        self.background = game_surface
        for i in range(randint(1, 10)):
            enemy = Enemy(randint(0, screen_width), randint(50, screen_height), self.player)
            self.enemy_group.add(enemy)

        for h in range(3):
            human = Humans(randint(75, 865), randint(80, screen_height - 80))
            self.human_group.add(human)

        self.score_text_rect = (150, 15)
        self.wave_number_rect = (415, 615)

    # Check if an event happens
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.player.shoot()

    # sets the collision between bullet and wall groups
    def bullet_collision(self):
        for wall in self.walls:
            for bullet in self.player.bullet_group:
                if pygame.sprite.collide_mask(bullet, wall):
                    bullet.kill()
        # clear the ball list
        self.player.bullet_list.clear()

    # sets the collision between player/wall/enemies groups
    def player_collision(self):
        for wall in self.walls:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(player, wall):
                    if abs(player.rect.top - wall.rect.bottom) < 50:
                        player.rect.y += player_speed
                    elif abs(wall.rect.top - player.rect.bottom) < 50:
                        player.rect.y -= player_speed
                    elif abs(wall.rect.left - player.rect.right) < 50:
                        player.rect.x -= player_speed
                    elif abs(player.rect.left - wall.rect.right) < 50:
                        player.rect.x += player_speed

    def player_damage(self):
        for enemy in self.enemy_group:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(enemy, player):
                    player.kill()
                    self.player.bullet_group.empty()
                    self.player.bullet_list.clear()

    def enemy_damage(self):
        for enemy in self.enemy_group:
            for bullet in self.player.bullet_group:
                if pygame.sprite.collide_mask(enemy, bullet):
                    bullet.kill()
                    enemy.kill()
                    self.player.score += 100
    
    def collect_humans(self):
        for human in self.human_group:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(player, human):
                    human.kill()
                    self.player.score += 2000

    def kill_humans(self):
        for human in self.human_group:
            for enemy in self.enemy_group:
                if pygame.sprite.collide_mask(enemy, human):
                    human.kill()

    def draw_borders(self):
        colour = choice(colour_list)
        pygame.draw.rect(self.screen, colour, (45, 45, 910, 10))
        pygame.draw.rect(self.screen, colour, (45, 600, 910, 10))
        pygame.draw.rect(self.screen, colour, (45, 45, 10, 555))
        pygame.draw.rect(self.screen, colour, (950, 45, 10, 565))

    # sets the game looping
    def game_loop(self):
        while self.loop:
            self.screen.blit(game_surface, (0, 0))
            self.check_events()
            self.draw_sprites()
            self.player.move()
            self.player_collision()
            self.player_damage()
            self.bullet_collision()
            self.enemy_damage()
            self.collect_humans()
            self.kill_humans()
            self.check_points()
            self.human_collide()
            self.draw_borders()

            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.update()
        self.player.update()
        self.player_sprites.draw(self.screen)
        self.player.bullet_group.draw(self.screen)
        self.player.bullet_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()
        self.human_group.draw(self.screen)
        self.human_group.update()

    def check_points(self):
        score_text = score_font.render(str(self.player.score), True, choice(colour_list))
        wave_text = score_font.render(str(self.player.wave_number) + " WAVE", True, choice(colour_list))
        self.screen.blit(score_text, self.score_text_rect)
        self.screen.blit(wave_text, self.wave_number_rect)

    def human_collide(self):
        for wall in self.walls:
            for human in self.human_group:
                if pygame.sprite.collide_mask(human, wall):
                    human.human_movement(True)
