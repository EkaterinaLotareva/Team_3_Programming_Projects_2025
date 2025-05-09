class View:
    def __init__(self, field, screen):
        self.field = field
        self.screen = screen
import pygame
import math

pass
#параметры экрана - ?
ROWS, COLS = 9, 12
WIDTH, HEIGHT = 1200, 900  

hex_height = HEIGHT / (ROWS * 3/4 + 1/4)  #высота гекса
hex_radius = hex_height/2   #радиус гекса
hex_width = hex_radius * 2 / math.sqrt(3)  #ширина гекса


offset_x = (WIDTH - (COLS - 1)*hex_width * 3/4 - hex_width)//2
offset_y = (HEIGHT - (ROWS - 1)* hex_height * 3/4 - hex_height)//2


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))    
clock = pygame.time.Clock()

#перевод в пиксели:
def pixelization(row, col):
    x = offset_x + col * hex_width * 3/4
    y = offset_y + row * hex_height * 3/4
    return int(x + hex_width / 2) , int(y + hex_height / 2)

#класс клеточки
class cell:
    def init(self, row, col, biome, building = None, animal = None):
        self.row = row
        self.col = col
        self.biome = biome
        self.building = building
        self.animal = animal

def drawing(surface, cell, images, hex_radius):
    x, y = pixelization(cell.row, cell.coll)

    biome_bild = images['biome'][cell.biome]
    biome_bild = pygame.transform.smoothscale(biome_bild, (int(hex_radius*1,7), int(hex_radius*1,7)))
    rect = biome_bild.get_rect(center = (x, y))
    surface.blit(biome_bild, rect)