import pygame 
import math
from field import Field
from config import *
from custom_types import *


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

    def to_pygame_coords(self, x, y):
        """С помощью этой функции мы можем двигать, все координаты (в Pygame идёт отсчёт с левого верхнего угла)"""
        pygame_x = x + offset_x_1
        pygame_y = -y + offset_y_1  # Инвертируем Y, чтобы ось смотрела вверх
        return (pygame_x, pygame_y)
    def new_coordinates(self, x_old, y_old): # Эта функция позволяет перейти от логических координат шестиугольников к тем визуальным
        x_new = x_old*(-1)*radius*3/2 + y_old*radius*3/2
        y_new = (x_old + y_old)*radius*(3**0.5)/2
        return (x_new, y_new)
    def calculate_hexagon_vertices(self, center_x, center_y, radius): #Эта функция позволяет рисовать через polygon
        """
    Возвращает список координат вершин правильного шестиугольника.
    Параметры:
        center_x (float): X-координата центра
        center_y (float): Y-координата центра
        radius (float): Радиус до вершин 
        
    Возвращает:
        list: Список кортежей с координатами вершин [(x1, y1), ..., (x6, y6)]
        """
        vertices = []
        for i in range(6):
            # Угол в градусах (60° между вершинами), начало с 0°
            angle_deg = 60 * i
        
            # Переводим угол в радианы
            angle_rad = math.radians(angle_deg)
        
            # Вычисляем координаты вершины
            x = center_x + radius * math.cos(angle_rad)
            y = center_y + radius * math.sin(angle_rad)

            vertices.append((round(x), round(y)))
    
        return vertices
    def draw_hexagon(self, i):
        pygame.draw.polygon(self.screen, color_green, self.calculate_hexagon_vertices(*self.to_pygame_coords(*new_coordinates(x_coord, y_coord)), radius)) # Рисует сам шестиугольник
        pygame.draw.polygon(self.screen, color_green, self.calculate_hexagon_vertices(*self.to_pygame_coords(*new_coordinates(x_coord, y_coord)), radius), 3) # Рисует обводку вокруг него
    def draw_field(self, field):
        for i in field.keys():
            self.draw_hexagon(i)


    def draw_circle(self, hex: coordinates, color):
        pass

    def draw_square(self, hex: coordinates, color):
        pass

    def from_pixels_to_logic(self, coords: coordinates):
        pass

