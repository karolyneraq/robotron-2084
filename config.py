import pygame

# looping
loop = True

# Colors
yellow = (255, 255, 0)

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

# sheets 
player_sheet = pygame.image.load("sprites/playersheet.png")
