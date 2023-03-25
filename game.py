from random import randint
from config import *
from player import Player
from enemys import Enemy
# from bullet import Bullet
pygame.init()


def draw(win, player, enemy_group, bullet_group):
    win.fill(BLACK)
    pygame.draw.rect(win, (255, 255, 0), (0, 50, WIDTH, HEIGHT - 50), 5)
    bullet_group.draw(win)
    player.draw(win)
    for curr_enemy in enemy_group:
        curr_enemy.draw(win)
    pygame.display.update()


def run_menu(menu):
    while menu:
        win.fill(BLACK)
        win.blit(play_img, (WIDTH // 2, (HEIGHT - 50) // 2))


def main():
    run = True
    menu = False
    clock = pygame.time.Clock()

    # run_menu(menu)

    enemy_group = pygame.sprite.Group()
    player = Player("player_img_front", WIDTH // 2, HEIGHT // 2, player_height, player_width)
    for cnt in range(randint(1, 10)):
        enemy = Enemy("enemy_img.png", randint(0, WIDTH), randint(50, HEIGHT))
        enemy_group.add(enemy)

    bullet_group = pygame.sprite.Group()
    while not menu:
        while run:
            clock.tick(FPS)
            draw(win, player, enemy_group, bullet_group)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bullet_group.add(player.create_bullet())

                    for curr_bullet in bullet_group:
                        if keys[pygame.K_w]:
                            curr_bullet.move_y(up=True)
                        if keys[pygame.K_s]:
                            curr_bullet.move_y(up=False)
                        if keys[pygame.K_d]:
                            curr_bullet.move_x(right=True)
                        if keys[pygame.K_a]:
                            curr_bullet.move_x(right=False)
            gets_hit = pygame.sprite.spritecollideany(player, enemy_group)
            print(gets_hit)
            keys = pygame.key.get_pressed()
            player.player_movement(keys, player, bullet_group)
            player.player_rotation(keys, player, win, player.x, player.y)
            enemy.enemy_movement(enemy_group, player)
            bullet_group.update()
        pygame.quit()


if __name__ == '__main__':
    main()
