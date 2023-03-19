import pygame

# looping
loop = True

# Colors
yellow = (255, 255, 0)
white = (255, 255, 255)

# screen height and width
screen_width = 1000
screen_height = 650

proportion = 100

# sets the game surface
game_surface = pygame.Surface((screen_width - proportion, screen_height - proportion))

border_width = 5

# clock 
clk = pygame.time.Clock()
fps = 60

# player
speed_player = 15.0

# bullets
speed_x_balls = 15.0
speed_y_balls = -15.0
reload_cooldown = 10

# player
speed_player = 15.0

# bullets
speed_x_balls = 15.5
speed_y_balls = -15.5
reload_cooldown = 15

# characters
shape_ppt = 40
