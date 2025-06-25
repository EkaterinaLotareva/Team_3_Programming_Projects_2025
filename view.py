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
        self.place_for_turn = pygame.Surface((round(WIDTH * 0.2), round(HEIGHT * 0.05)))

        r = 2 * radius
        r_ = 2 * radius * np.cos(np.deg2rad(30))

        image_of_sea = pygame.transform.smoothscale(pygame.image.load('images_of_field/Вода.png').convert_alpha(),
                                                    (r, r_))
        image_of_desert = pygame.transform.smoothscale(pygame.image.load('images_of_field/Пустыня.png').convert_alpha(),
                                                       (r, r_))
        image_of_swamp = pygame.transform.smoothscale(pygame.image.load('images_of_field/Болото.png').convert_alpha(),
                                                      (r, r_))
        image_of_forest = pygame.transform.smoothscale(pygame.image.load('images_of_field/Лес.png').convert_alpha(),
                                                       (r, r_))
        image_of_mountains = pygame.transform.smoothscale(pygame.image.load('images_of_field/Горы.png').convert_alpha(),
                                                          (r, r_))

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
        x_new = (coords[0] * (-1) * radius * 3 / 2 + coords[1] * radius * 3 / 2) + offset_x_1
        y_new = (-1) * ((coords[0] + coords[1]) * radius * (3 ** 0.5) / 2) + offset_y_1
        return (x_new, y_new)

    def from_pixels_to_logic(self, coords: coordinates):
        '''Эта функция принимает (x, y), координаты пикселя и возвращает координаты шестиугольника'''
        for i in self.field.hex.keys():
            centr_of_hex_cooords = self.from_logic_to_pixels(i)
            distance = ((centr_of_hex_cooords[0] - coords[0]) ** 2 + (centr_of_hex_cooords[1] - coords[1]) ** 2) ** 0.5
            if distance < radius:
                return i
        return (-10, -10)

    def calculate_n_verticles(self, coords: coordinates, Radius, n):
        '''Данная функция позволяет находить координаты вершин n-угольника, зная его центр и размеры.
        Используется для отрисовки обводки, постройки строений, квадратов и кругов.'''
        verticles = []
        for i in range(n):
            angle_deg = 360 / n * i
            angle_rad = np.deg2rad(angle_deg)
            x = coords[0] + Radius * math.cos(angle_rad)
            y = coords[1] + Radius * math.sin(angle_rad)
            verticles.append((round(x), round(y)))

        return verticles

    def calculate_square_verticles(self, coords: coordinates, Radius):
        verticles = []
        verticles.append((round(coords[0] + Radius / (2) ** 0.5), round(coords[1] + Radius / (2) ** 0.5)))
        verticles.append((round(coords[0] - Radius / (2) ** 0.5), round(coords[1] + Radius / (2) ** 0.5)))
        verticles.append((round(coords[0] - Radius / (2) ** 0.5), round(coords[1] - Radius / (2) ** 0.5)))
        verticles.append((round(coords[0] + Radius / (2) ** 0.5), round(coords[1] - Radius / (2) ** 0.5)))
        return verticles

    def draw_hexagon(self, Coordinates: coordinates, hex: Hex):
        '''Данная функция отрисовывает, отдельно взятый шестиугольник со всеми объектами'''
        coords = self.from_logic_to_pixels(Coordinates)
        self.screen.blit(self.image_dict[hex.zone],
                         (coords[0] - radius, coords[1] - round((radius) * np.cos(np.deg2rad(30)))))
        if hex.animal != None:
            if hex.animal == 'jaguar':
                pygame.draw.polygon(self.screen, ORANGE,
                                    self.calculate_n_verticles(coords, radius - math.ceil(radius / 11), 6), radius // 6)
            elif hex.animal == 'bear':
                pygame.draw.polygon(self.screen, BROWN,
                                    self.calculate_n_verticles(coords, radius - math.ceil(radius / 11), 6), radius // 6)
        if hex.building != None:
            if hex.building[1] == 'hut':
                pygame.draw.polygon(self.screen, self.logic_colors_to_rgb(hex.building[0]),
                                    self.calculate_n_verticles(coords, radius // 2.5, 3))
            elif hex.building[1] == 'monument':
                pygame.draw.polygon(self.screen, self.logic_colors_to_rgb(hex.building[0]),
                                    self.calculate_n_verticles(coords, radius // 2.5, 6))
        pygame.draw.polygon(self.screen, BLACK, self.calculate_n_verticles(coords, radius, 6), radius // 6)

    def draw_turn(self, player: int):
        '''пишет на основном экране надпись 'ход игрока (player)' '''
        self.place_for_turn.fill(BLACK)
        s = 'Ход игрока ' + str(player)
        # print(s)
        text_of_turn = f1.render(s, True, WHITE)
        self.place_for_turn.blit(text_of_turn, (0, 0))
        self.screen.blit(self.place_for_turn, (round(WIDTH * 0.02), round(HEIGHT * 0.04)))
        pygame.display.update()

    def draw_legend(self):
        text_heading = f1.render('Легенда карты', True,
                                 (255, 255, 255))
        text_swamp = f2.render('Болото', True, (255, 255, 255))
        text_sea = f2.render('Море', True, (255, 255, 255))
        text_mountains = f2.render('Горы', True, (255, 255, 255))
        text_forest = f2.render('Лес', True, (255, 255, 255))
        text_desert = f2.render('Пустыня', True, (255, 255, 255))
        text_huts = f2.render('Хижины', True, WHITE)
        text_monuments = f2.render('Монументы', True, WHITE)
        text_jaguars_1 = f2.render('Поля c', True, WHITE)
        text_jaguars_2 = f2.render('ягуарами', True, WHITE)
        text_bears = f2.render('медведями', True, WHITE)
        self.screen.blit(text_heading, (round(0.75 * WIDTH), 0.11 * HEIGHT))
        self.screen.blit(self.image_dict['water'], (round(0.67 * WIDTH), round(0.18 * HEIGHT)))
        self.screen.blit(text_sea, (round(0.73 * WIDTH), round(0.18 * HEIGHT)))
        self.screen.blit(self.image_dict['swamp'], (round(0.77 * WIDTH), round(0.18 * HEIGHT)))
        self.screen.blit(text_swamp, (round(0.83 * WIDTH), round(0.18 * HEIGHT)))
        self.screen.blit(self.image_dict['desert'], (round(0.87 * WIDTH), round(0.18 * HEIGHT)))
        self.screen.blit(text_desert, (round(0.93 * WIDTH), round(0.18 * HEIGHT)))
        self.screen.blit(self.image_dict['forest'], (round(0.72 * WIDTH), round(0.28 * HEIGHT)))
        self.screen.blit(text_forest, (round(0.78 * WIDTH), round(0.28 * HEIGHT)))
        self.screen.blit(self.image_dict['mountain'], (round(0.82 * WIDTH), round(0.28 * HEIGHT)))
        self.screen.blit(text_mountains, (round(0.88 * WIDTH), round(0.28 * HEIGHT)))
        self.screen.blit(text_huts, (round(0.75 * WIDTH), round(0.42 * HEIGHT)))
        self.screen.blit(text_jaguars_1, (round(0.91 * WIDTH), round(0.51 * HEIGHT)))
        self.screen.blit(text_jaguars_2, (round(0.91 * WIDTH), round(0.53 * HEIGHT)))
        self.screen.blit(text_jaguars_1, (round(0.77 * WIDTH), round(0.51 * HEIGHT)))
        self.screen.blit(text_bears, (round(0.77 * WIDTH), round(0.53 * HEIGHT)))
        self.screen.blit(text_monuments, (round(0.87 * WIDTH), round(0.42 * HEIGHT)))
        pygame.draw.polygon(self.screen, GREEN,
                            self.calculate_n_verticles((round(0.72 * WIDTH), round(0.43 * HEIGHT)), radius // 1.2, 3))
        # pygame.draw.polygon(self.screen, WHITE, self.calculate_n_verticles((round(0.72*WIDTH), round(0.43*HEIGHT)), radius // 1.2, 3))
        # pygame.draw.polygon(self.screen, BLUE, self.calculate_n_verticles((round(0.77*WIDTH), round(0.43*HEIGHT)), radius // 1.2, 3))
        # pygame.draw.polygon(self.screen, WHITE, self.calculate_n_verticles((round(0.81*WIDTH), round(0.52*HEIGHT)), radius // 1.2, 6))
        # pygame.draw.polygon(self.screen, GREEN, self.calculate_n_verticles((round(0.87*WIDTH), round(0.52*HEIGHT)), radius // 1.2, 6))
        pygame.draw.polygon(self.screen, BLUE,
                            self.calculate_n_verticles((round(0.84 * WIDTH), round(0.43 * HEIGHT)), radius // 1.2, 6))
        self.screen.blit(self.image_dict['mountain'], (round(0.84 * WIDTH), round(0.5 * HEIGHT)))
        pygame.draw.polygon(self.screen, ORANGE,
                            self.calculate_n_verticles((round(0.84 * WIDTH) + radius, round(0.5 * HEIGHT) + radius_vp),
                                                       radius - math.ceil(radius / 27), 6), radius // 8)
        self.screen.blit(self.image_dict['desert'], (round(0.70 * WIDTH), round(0.5 * HEIGHT)))
        pygame.draw.polygon(self.screen, BROWN,
                            self.calculate_n_verticles((round(0.70 * WIDTH) + radius, round(0.5 * HEIGHT) + radius_vp),
                                                       radius, 6), radius // 8)
        pygame.display.update()

    def draw_buttons(self):
        text_hints = f2.render('Подсказки', True, WHITE)
        text_rules = f2.render('Правила', True, WHITE)
        pygame.draw.rect(self.screen, GREY, (WIDTH * 0.70, 0.63 * HEIGHT, WIDTH * 0.1, HEIGHT * 0.08))
        pygame.draw.rect(self.screen, GREY, (WIDTH * 0.83, 0.63 * HEIGHT, WIDTH * 0.1, HEIGHT * 0.08))
        self.screen.blit(text_hints, (WIDTH * 0.72, HEIGHT * 0.66))
        self.screen.blit(text_rules, (WIDTH * 0.86, HEIGHT * 0.66))
        pygame.display.update

    def draw_field(self):
        for i in self.field.hex.keys():
            self.draw_hexagon(i, self.field.hex[i])
        self.draw_legend()
        self.draw_buttons()
        self.draw_turn(1)
        pygame.display.update()

    def draw_circle(self, coords: coordinates, color):
        r = radius // 4
        pygame.draw.circle(self.screen, color, (coords[0], coords[1]), r)
        pygame.display.update()

    def draw_square(self, coords: coordinates, color):
        r = radius // 4
        pygame.draw.polygon(self.screen, color, self.calculate_square_verticles((coords[0], coords[1]), r))
        pygame.display.update()

    def greeting_screen(self):
        '''отрисовка приветственного экрана с краткими правилами игры, с надписью 'выберите количество игроков' и тремя
         кнопками : 3, 4 и 5, и кнопкой 'продолжить' '''
        self.screen.fill((0, 0, 0))
        f1 = pygame.font.Font(None, 44)
        text_heading = f1.render('Криптид', True,
                                 (255, 255, 255))
        self.screen.blit(text_heading, (400, 500))

    def choose_number_of_players_button(self, coords: coordinates):
        '''обработка нажатия на кнопки с количеством игроков на приветственном экране. возвращает None, если координаты
        не попадают ни в одну из кнопок, а если попадают, то возвражает число, написанное на кнопке (3, 4 или 5)'''
        pass

    def to_game_button(self, coords: coordinates):
        '''обработка нажатия на кнопку 'продолжить' на приветственном экране: возвращает True если координаты (coords)
           попадают в кнопку и False если не попадают. так же должны работать все остальные функции, отрабатывающие
           нажатие на кнопку, то есть функции, в названии которых есть слово button и которые принимают на вход координаты'''
        pass

    def hint_screen(self):
        '''экран с подсказками, на котором написаны строчки: 'подсказка игрока номер N' для каждого игрока, с кнопками
         'показать подсказку' и 'скрыть подсказку' для каждого игрока'''
        pass

    def show_hint_button(self, coords: coordinates):
        '''обработка нажатия на кнопку 'показать подсказку' (одну из трех) на экране с подсказками (hint_screen)'''
        pass

    def hide_hint_button(self, coords: coordinates):
        '''обработка нажатия на кнопку 'скрыть подсказку' (одну из трех) на экране с подсказками (hint_screen)'''
        pass

    def show_hint(self, player: int):
        '''пишет подсказку игрока под номером 'player' на экране с подсказками (hint_screen)'''
        pass

    def hide_hint(self, player: int):
        '''убирает подсказку игрока под номером 'player' с экрана с подсказками'''
        pass

    def side_notes(self):
        '''рисует на экране все, что должно там быть помимо поля. поле должно быть слева, а справа - краткая подсказка
        с легендой карты, надпись чей сейчас ход и кнопка 'посмотреть подсказки' '''
        pass

    def from_game_to_hint_screen_button(self, coords: coordinates):
        '''обработка нажатия на кнопку, возвращающую на экран с подсказками'''
        pass








