import pygame 
import math
import numpy as np
from field import Field, Hex
from config import *
from custom_types import *



class View:

    def __init__(self, field: Field, screen: pygame.surface.Surface):
        self.field = field
        self.screen = screen


    def from_logic_to_pixels(self, coords: coordinates):   
        x_new = (coords[0]*(-1)*radius*3/2 + coords[1]*radius*3/2) + offset_x  # Эта функция позволяет перейти от логических координат шестиугольников к визуальным, то есть пикселям
        y_new = (-1)*((coords[0] + coords[1])*radius*(3**0.5)/2) + offset_y
        return (x_new, y_new)
    

    def from_pixels_to_logic(self, coords: coordinates):
        for i in self.field.hex.keys():
            centr_of_hex_cooords = self.from_logic_to_pixels(*coords) # Эта функция принимает (x, y), координаты пикселя и возвращает координаты шестиугольника
            distance = ((centr_of_hex_cooords[0] - coords[0])**2 + (centr_of_hex_cooords[1] - coords[1])**2)**0.5                                                   
            if distance < radius:
                return (i[0], i[1])
        return (-10, -10)
    

    def calculate_n_verticles(self, coords: coordinates, Radius, n):
        verticles = []
        for i in range(n):
            angle_deg = 360/n * i
            angle_rad = np.deg2rad(angle_deg)
            x = coords[0] + Radius * math.cos(angle_rad) # Данная функция позволяет находить координаты вершин n-угольника, зная его центр и размеры.
            y = coords[1] + Radius * math.sin(angle_rad) # Используется для отрисовки обводки, постройки строений, квадратов и кругов.

        verticles.append((round(x), round(y)))
        return verticles
    
    def calculate_square_verticles(self, coords:coordinates, Radius):
        verticles = []
        verticles.append((round(coords[0] + Radius/(2)**0.5), round(coords[1] + Radius/(2)**0.5)))
        verticles.append((round(coords[0] - Radius/(2)**0.5), round(coords[1] + Radius/(2)**0.5)))
        verticles.append((round(coords[0] - Radius/(2)**0.5), round(coords[1] - Radius/(2)**0.5)))
        verticles.append((round(coords[0] + Radius/(2)**0.5), round(coords[1] - Radius/(2)**0.5)))
        return verticles

    def draw_hexagon(self, Coordinates: coordinates, hex: Hex):
        coords = self.from_logic_to_pixels(*Coordinates)
        self.screen.blit(image_dict[hex.zone], (coords[0] - radius, coords[1] - round((radius)*np.cos(np.deg2rad(30)))))
        if hex.animal != None:
            if hex.animal == 'ягуар':
                pygame.draw.polygon(self.screen, color_orange, self.calculate_n_verticles(*coords, radius - 5, 6), 5)
            else:
                pygame.draw.polygon(self.screen, color_brown, self.calculate_n_verticles(*coords, radius - 5, 6), 5)   # Данная функция отрисовывает, отдельно взятый шестиугольник.
        if hex.building != None:                                                                                       # Сразу же рисуются ягуары/медведи и здания.
            if hex.building[0] == 'hunt':
                pygame.draw.polygon(self.screen, hex.building[1], self.calculate_n_verticles(*coords, radius // 2.5, 3))
            else:
                pygame.draw.polygon(self.screen, hex.building[1], self.calculate_n_verticles(*coords, radius // 2.5, 6))
        pygame.draw.polygon(self.screen, color_white, self.calculate_n_verticles(*coords, radius, 6), 5)               # Рисуется разделение между клетками


    def draw_field(self):
        for i in self.field.hex.keys():                         # Данная, функция должна отрисовывать всё поле
            self.draw_hexagon(i, self.field.hex[i])

    def draw_circle(self, coords: coordinates, color):
        r = radius // 6
        if color == RED:
            pygame.draw.circle(self.screen, color, (self.from_logic_to_pixels(coords)[0], self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        elif color == BLUE:
            pygame.draw.circle(self.screen, color, (self.from_logic_to_pixels(coords)[0] + radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        else:
            pygame.draw.circle(self.screen, color, (self.from_logic_to_pixels(coords)[0] - radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)

    def draw_square(self, coords: coordinates, color):
        r = radius // 6
        if color == RED:
            pygame.draw.polygon(self.screen, color, self.calculate_square_verticles(self.from_logic_to_pixels(coords)[0], self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        elif color == BLUE:
            pygame.draw.polygon(self.screen, color, self.calculate_square_verticles(self.from_logic_to_pixels(coords)[0] + radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        else:
            pygame.draw.polygon(self.screen, color, self.calculate_square_verticles(self.from_logic_to_pixels(coords)[0] - radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)




