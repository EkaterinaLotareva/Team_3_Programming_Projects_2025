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


        r = 2 * radius
        r_ = 2 * radius * np.cos(np.deg2rad(30))

        image_of_sea = pygame.transform.smoothscale(pygame.image.load('images_of_field/Вода.png').convert_alpha(), (r, r_))
        image_of_desert = pygame.transform.smoothscale(pygame.image.load('images_of_field/Пустыня.png').convert_alpha(), (r, r_))
        image_of_swamp = pygame.transform.smoothscale(pygame.image.load('images_of_field/Болото.png').convert_alpha(), (r, r_))
        image_of_forest = pygame.transform.smoothscale(pygame.image.load('images_of_field/Лес.png').convert_alpha(), (r, r_))
        image_of_mountains = pygame.transform.smoothscale(pygame.image.load('images_of_field/Горы.png').convert_alpha(), (r, r_))

        self.image_dict = {'desert': image_of_desert,  # Словарь,связывающий зону и соответствующую ей картинку
                      'water': image_of_sea,
                      'swamp': image_of_swamp,
                      'mountain': image_of_mountains,
                      'forest': image_of_forest}

    def logic_colors_to_rgb(self, color: Color):
        if color == 'white':
            return WHITE
        elif color == 'green':
            return GREEN
        elif color == 'blue':
            return BLUE

    def from_logic_to_pixels(self, coords: coordinates):
        '''Эта функция позволяет перейти от логических координат шестиугольников к визуальным, то есть пикселям'''
        x_new = (coords[0]*(-1)*radius*3/2 + coords[1]*radius*3/2) + offset_x_1
        y_new = (-1)*((coords[0] + coords[1])*radius*(3**0.5)/2) + offset_y_1
        return (x_new, y_new)
    

    def from_pixels_to_logic(self, coords: coordinates):
        '''Эта функция принимает (x, y), координаты пикселя и возвращает координаты шестиугольника'''
        for i in self.field.hex.keys():
            centr_of_hex_cooords = self.from_logic_to_pixels(i)
            distance = ((centr_of_hex_cooords[0] - coords[0])**2 + (centr_of_hex_cooords[1] - coords[1])**2)**0.5                                                   
            if distance < radius:
                return i
        return (-10, -10)
    

    def calculate_n_verticles(self, coords: coordinates, Radius, n):
        '''Данная функция позволяет находить координаты вершин n-угольника, зная его центр и размеры.
        Используется для отрисовки обводки, постройки строений, квадратов и кругов.'''
        verticles = []
        for i in range(n):
            angle_deg = 360/n * i
            angle_rad = np.deg2rad(angle_deg)
            x = coords[0] + Radius * math.cos(angle_rad)
            y = coords[1] + Radius * math.sin(angle_rad)
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
        '''Данная функция отрисовывает, отдельно взятый шестиугольник со всеми объектами'''
        coords = self.from_logic_to_pixels(Coordinates)
        self.screen.blit(self.image_dict[hex.zone], (coords[0] - radius, coords[1] - round((radius)*np.cos(np.deg2rad(30)))))
        if hex.animal != None:
            if hex.animal == 'jaguar':
                pygame.draw.polygon(self.screen, ORANGE, self.calculate_n_verticles(coords, radius - 5, 6), 5)
            elif hex.animal == 'bear':
                pygame.draw.polygon(self.screen, BROWN, self.calculate_n_verticles(coords, radius - 5, 6), 5)
        if hex.building != None:
            if hex.building[1] == 'hut':
                pygame.draw.polygon(self.screen, self.logic_colors_to_rgb(hex.building[0]), self.calculate_n_verticles(coords, radius // 2.5, 3))
            elif hex.building[1] == 'monument':
                pygame.draw.polygon(self.screen, self.logic_colors_to_rgb(hex.building[0]), self.calculate_n_verticles(coords, radius // 2.5, 6))
        pygame.draw.polygon(self.screen, BLACK, self.calculate_n_verticles(coords, radius, 6), 5)


    def draw_field(self):
        for i in self.field.hex.keys():
            self.draw_hexagon(i, self.field.hex[i])
        pygame.display.update()


    def draw_circle(self, coords: coordinates, color):
        r = radius // 6
        if color == RED:
            pygame.draw.circle(self.screen, color, (self.from_logic_to_pixels(coords)[0], self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        elif color == BLUE:
            pygame.draw.circle(self.screen, color, (self.from_logic_to_pixels(coords)[0] + radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        else:
            pygame.draw.circle(self.screen, color, (self.from_logic_to_pixels(coords)[0] - radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r)
        pygame.display.update()

    def draw_square(self, coords: coordinates, color):
        r = radius // 10
        if color == RED:
            pygame.draw.polygon(self.screen, color, self.calculate_square_verticles((self.from_logic_to_pixels(coords)[0], self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r))
        elif color == BLUE:
            pygame.draw.polygon(self.screen, color, self.calculate_square_verticles((self.from_logic_to_pixels(coords)[0] + radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r))
        else:
            pygame.draw.polygon(self.screen, color, self.calculate_square_verticles((self.from_logic_to_pixels(coords)[0] - radius // 6, self.from_logic_to_pixels(coords)[1] + round(0.6*radius * np.sin(np.deg2rad(60)))), r))
        pygame.display.update()



