# settings.py

# Constants
import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
CELL_SIZE = 40
FPS = 60

# Load images
PATH_IMAGE = pygame.image.load('assets/grass.png')
WALL_IMAGE = pygame.image.load('assets/wall.jpeg')
PLAYER_IMAGE = pygame.image.load('assets/char.png')
FINISH_IMAGE = pygame.image.load('assets/finish.png')

# Resize images to fit cell size
PATH_IMAGE = pygame.transform.scale(PATH_IMAGE, (CELL_SIZE, CELL_SIZE))
WALL_IMAGE = pygame.transform.scale(WALL_IMAGE, (CELL_SIZE, CELL_SIZE))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))
FINISH_IMAGE = pygame.transform.scale(FINISH_IMAGE, (CELL_SIZE, CELL_SIZE))

# Messages
FINAL_CELL_MESSAGE = "You won!"
INFO_MESSAGE = "R for restart, E for exit."
