import pygame 
import math
import field
from config import ROWS, COLS, WIDTH, HEIGHT, hex_height, hex_radius, hex_width, offset_x, offset_y 


class View:

    def __init__(self, field, screen): #филд - словарь
        self.field = field
        self.screen = screen

    #перевод в пиксели:
    def pixelization(self, row, col):
        x = offset_x + hex_width/2 + (cols-1)*hex_width
        y = offset_y + (hex_height/2)*cols + (rows-1)*hex_height
        return x, y 


    def draw_hex(self, surface, row, col):
        x, y = self.pixelization(row, col)
        pygame.circle(surface, (x, y), hex_radius)

    def transform_coords(self, row, col):
    # переводит смещенные координаты в осевые
        y_new = 5 - (row - 1) + (col - col/2 - 0.5)*(0 ** (1 - (col % 2))) + (col - col/2 - 1)*(0 ** (col % 2))
        x_new = 11 - (row -1) - (col - col/2 - 0.5)*(0 ** (1 - (col % 2))) - (col - col/2 - 1)*(0 ** (col % 2))

    def draw_field(self, surface, field):
        for i in range(ROWS):
            for j in range(COLS):
                axis_coords = self.transform_coords((i, j))
                hex = field[axis_coords]
                self.drawing(surface, hex, i, j)
