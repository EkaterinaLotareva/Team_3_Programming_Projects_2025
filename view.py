import pygame 
import math
from field import Field
from config import ROWS, COLS, WIDTH, HEIGHT, hex_height, hex_radius, hex_width, offset_x, offset_y, BLACK


class View:

    def __init__(self, field: Field, screen):
        self.field = field
        self.screen = screen

    def transform_coords(self, row, col):
        '''переводит смещенные координаты (используемые в визуализации) в осевые (используемые в логике)'''
        y_new = 5 - (row - 1) + (col - col/2 - 0.5)*(0 ** (1 - (col % 2))) + (col - col/2 - 1)*(0 ** (col % 2))
        x_new = 11 - (row - 1) - (col - col/2 - 0.5)*(0 ** (1 - (col % 2))) - (col - col/2 - 1)*(0 ** (col % 2))
        return x_new, y_new

    def pixelization(self, row, col):
        '''перевод координат гекса на поле в координаты пикселя на экране'''
        x = offset_x + hex_width/2 + (col-1)*hex_width
        y = offset_y + (hex_height/2)*col + (row-1)*hex_height
        return x, y

    def draw_hex(self, surface, row, col):      # пока рисует одинаковые кружочки вместо шестиугольников
        x, y = self.pixelization(row, col)
        pygame.draw.circle(surface, color=BLACK, center=(x, y), radius=hex_radius)

    def draw_field(self, surface, field):
        for i in range(ROWS):
            for j in range(COLS):
                self.draw_hex(surface, i, j)

