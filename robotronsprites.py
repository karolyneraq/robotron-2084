import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robotron")
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# sizes
player_width = 22
player_height = 32
width28 = 28
height36 = 36
no_34 = 34

# Images
player_img_front = pygame.transform.scale(pygame.image.load('assets/player_front.png'), (22, 32))
player_img_left = pygame.transform.scale(pygame.image.load('assets/player_left.png'), (22, 32))
player_img_right = pygame.transform.scale(pygame.image.load('assets/player_right.png'), (22, 32))
player_img_back = pygame.transform.scale(pygame.image.load('assets/player_back.png'), (22, 32))
enemy_img = pygame.transform.scale(pygame.image.load('assets/enemy_img.png'), (32, 32))
play_img = pygame.image.load('assets/play.png')

# Hit boxes
# player_rect = pygame.draw.rect(win, (0, 0, 255,), player.hit_box, 2)
# enemy_rect = pygame.draw.rect(win, (255, 0, 0), enemy.hit_box, 2)


class Player(pygame.sprite.Sprite):
	player_vel = 3
	player_width = 1
	player_height = 1

	def __init__(self, image, x, y, height, width):
		super().__init__()
		self.x = self.origin_x = x
		self.y = self.origin_y = y
		self.width = player_width
		self.height = player_height
		self.hit_box = (self.x - 2, self.y - 2, 28, 36)
		self.image = player_img_front
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def move_x(self, right=True):
		if right:
			self.x -= self.player_vel
		else:
			self.x += self.player_vel

	def move_y(self, up=True):
		if up:
			self.y -= self.player_vel
		else:
			self.y += self.player_vel

	def draw(self, win):
		self.hit_box = (self.x - 2, self.y - 2, 28, 36)
		# pygame.draw.rect(win, (255,0,0), self.hit_box,2)
		win.blit(player_img_front, (self.x, self.y))

	def create_bullet(self):
		return Bullet(self.x, self.y)


class Enemy(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.enemy_vel = 1
		self.hit_box = (self.x, self.y, 34, 34)
		self.image = enemy_img
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def move_x(self, right=True):
		if right:
			self.x += self.enemy_vel
		else:
			self.x -= self.enemy_vel

	def move_y(self, above=True):
		if above:
			self.y += self.enemy_vel
		else:
			self.y -= self.enemy_vel

	def draw(self, win):
		self.hit_box = (self.x, self.y, 34, 34)
		# pygame.draw.rect(win, (0,255,0), self.hit_box, 2)
		win.blit(enemy_img, (self.x, self.y))


def draw(win, player, enemy_group, bullet_group):
	win.fill(BLACK)
	pygame.draw.rect(win, (255, 255, 0), (0, 50, WIDTH, HEIGHT-50), 5)
	bullet_group.draw(win)
	player.draw(win)
	for curr_enemy in enemy_group:
		curr_enemy.draw(win)
	pygame.display.update()


def player_rotation(keys, player, win, x, y):
	if keys[pygame.K_w]:
		win.blit(player_img_back, (x, y))
	if keys[pygame.K_s]:
		win.blit(player_img_front, (x, y))
	if keys[pygame.K_d]:
		win.blit(player_img_right, (x, y))
	if keys[pygame.K_a]:
		win.blit(player_img_left, (x, y))
	pygame.display.update()


def player_movement(keys, player, bullet):
	if keys[pygame.K_w] and player.y - player.player_vel - 1 > 53:
		player.move_y(up=True)
	if keys[pygame.K_s] and player.y + player.player_vel + 32 + 1 <= HEIGHT:
		player.move_y(up=False)

	if keys[pygame.K_a] and player.x - player.player_vel - 1 >= 0:
		player.move_x(right=True)

	if keys[pygame.K_d] and player.x + player.player_vel + 32 - 8 <= WIDTH:
		player.move_x(right=False)


def enemy_movement(enemy_group, player):
	for curr_enemy in enemy_group:
		if player.y >= curr_enemy.y:
			curr_enemy.move_y(above=True)
		if player.y <= curr_enemy.y:
			curr_enemy.move_y(above=False)
		if player.x >= curr_enemy.x:
			curr_enemy.move_x(right=True)
		if player.x <= curr_enemy.x:
			curr_enemy.move_x(right=False)


def bullet_movement_1(keys, bullet_group):
	for curr_bullet in bullet_group:
		if keys[pygame.K_w]:
			curr_bullet.move_y(up=True)
		if keys[pygame.K_s]:
			curr_bullet.move_y(up=False)
		if keys[pygame.K_d]:
			curr_bullet.move_x(right=True)
		if keys[pygame.K_a]:
			curr_bullet.move_x(right=False)


def bullet_movement(bullet):
	bullet.rect.x += bullet_vel


class Bullet(pygame.sprite.Sprite):
	bullet_vel = 5

	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((3, 3))
		self.image.fill((255, 0, 0))
		self.rect = self.image.get_rect(center=(x, y))

	def move_x(self, right=True):
		if right:
			self.rect.x += self.bullet_vel
		else:
			self.rect.x -= self.bullet_vel

	def move_y(self, up=True):
		if up:
			self.rect.y -= self.bullet_vel
		else:
			self.rect.y += self.bullet_vel
	
	def update(self):
		if self.rect.x >= WIDTH + 3 or self.rect.x <= -3:
			self.kill()

		elif self.rect.y >= HEIGHT + 3 or self.rect.y <= -3:
			self.kill()

	def draw(self, win):
		win.blit(self.image, (self.x, self.y))


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
			player_movement(keys, player, bullet_group)
			player_rotation(keys, player, win, player.x, player.y)
			enemy_movement(enemy_group, player)
			bullet_group.update()
		pygame.quit()


if __name__ == '__main__':
	main()
