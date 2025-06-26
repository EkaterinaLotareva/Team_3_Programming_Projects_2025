import math
import pygame
import numpy as np
ROWS, COLS = 9, 12
pygame.init()
size_of_screen = pygame.display.get_desktop_sizes()[0]
WIDTH = size_of_screen[0]
HEIGHT = size_of_screen[1]
hex_height = HEIGHT / (ROWS * 3/4 + 1/4)  #высота гекса
hex_radius = hex_height/2   #радиус гекса
hex_width = hex_radius * 2 / math.sqrt(3)  #ширина гекса

radius = (WIDTH + HEIGHT) // 55
radius_vp = round(radius * 3**(0.5)) // 2 # размер шестиугольника
offset_x_1 = WIDTH // 2.9
offset_y_1 = HEIGHT // 1.2

offset_x = (WIDTH - (COLS - 1)*hex_width * 3/4 - hex_width)//2
offset_y = (HEIGHT - (ROWS - 1)* hex_height * 3/4 - hex_height)//2

f1 = pygame.font.Font(None, round(44 * (WIDTH + HEIGHT) / (1920 + 1080)))
f2 = pygame.font.Font(None, round(30 * (WIDTH + HEIGHT) / (1920 + 1080)))

BLACK = (0, 0, 0)
TURQUOUISE = (64, 224, 208)
NEW_COLOR = (14, 118, 130)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)
WHITE = (255, 255, 255)
GREY = (41, 49, 51)
ORANGE = (251, 139, 35)