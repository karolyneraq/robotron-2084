from random import randint
from config import *
from enemy import Enemy
from player import Player
from layouts import Layouts

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player_sprites = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.player = Player((500, 300), player)
        self.player_sprites.add(self.player)
        self.background = game_surface
        for i in range(randint(1, 10)):
            enemy = Enemy(randint(0, screen_width), randint(50, screen_height), self.player)
            self.enemy_group.add(enemy)
        self.score_text_rect = (45, 5)

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

    # sets the collision between player/wall/enemie groups
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


    def enemy_damage(self):
        for enemy in self.enemy_group:
            for bullet in self.player.bullet_group:
                if pygame.sprite.collide_mask(enemy, bullet):
                    enemy.kill()
                    self.player.score += 100

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
            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.draw(self.screen)
        self.player.update()
        self.player_sprites.draw(self.screen)
        self.player.bullet_group.draw(self.screen)
        self.player.bullet_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()

   