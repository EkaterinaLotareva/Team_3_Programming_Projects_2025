import pygame
import math
import numpy as np
from field import Field, Hex, BuildingTypeHint, BuildingColorHint
from config import *
from custom_types import *


class View:

    def __init__(self, field: Field, screen: pygame.surface.Surface):
        self.field = field
        self.screen = screen
        self.place_for_turn = pygame.Surface((round(WIDTH * 0.2), round(HEIGHT * 0.05)))
        self.place_for_text = pygame.Surface((round(WIDTH *0.55), round(HEIGHT * 0.05)))
        r = 2 * radius
        r_ = 2 * radius * np.cos(np.deg2rad(30))
        image_of_sea = pygame.transform.smoothscale(pygame.image.load('images_of_field/Вода.png').convert_alpha(), (r, r_))
        image_of_desert = pygame.transform.smoothscale(pygame.image.load('images_of_field/Пустыня.png').convert_alpha(),
                                                       (r, r_))
        image_of_swamp = pygame.transform.smoothscale(pygame.image.load('images_of_field/Болото.png').convert_alpha(),
                                                            (r, r_))
        image_of_forest = pygame.transform.smoothscale(pygame.image.load('images_of_field/Лес.png').convert_alpha(),
                                                            (r, r_))
        image_of_mountains = pygame.transform.smoothscale(pygame.image.load('images_of_field/Горы.png').convert_alpha(),
                                                                (r, r_))
        image_of_cryptid_1 = pygame.image.load('images_of_field/Криптид_картинка 1.png').convert_alpha()
                
        image_of_cryptid_2 = pygame.image.load('images_of_field/Криптид картинка 2.png').convert_alpha()

        cryptid_text = pygame.image.load('images_of_field/Криптид надпись.png').convert_alpha()

        game_start = pygame.image.load('images_of_field/Начать игру надпись.png').convert_alpha()

        game_start_button = pygame.image.load('images_of_field/Начать игру кнопка.png').convert_alpha()

        rules = pygame.image.load('images_of_field/Правила надпись.png').convert_alpha()

        rules_button = pygame.image.load('images_of_field/Правила_криптид.png').convert_alpha()

        rules_zones = pygame.image.load('images_of_field/Правила_зоны.png').convert_alpha()

        rules_zones_2 = pygame.image.load('images_of_field/Правила_зоны_2.png').convert_alpha()

        exit = pygame.image.load('images_of_field/Выход.png').convert_alpha()

        self.image_of_cryptid_1 = pygame.transform.smoothscale(image_of_cryptid_1, (round(image_of_cryptid_1.get_width()*(1.1*WIDTH / 1920)), 
                                                                                        round(image_of_cryptid_1.get_height()*(1.1*HEIGHT / 1080))))
        self.image_of_cryptid_2 = pygame.transform.smoothscale(image_of_cryptid_2, (round(image_of_cryptid_2.get_width()*(1.1*WIDTH / 1920)), 
                                                                                        round(image_of_cryptid_2.get_height()*(1.1*HEIGHT / 1080))))
        self.cryptid_text = pygame.transform.smoothscale(cryptid_text, (round(cryptid_text.get_width()*(WIDTH / 1920)), round(cryptid_text.get_height()*(HEIGHT / 1080))))

        self.game_start = pygame.transform.smoothscale(game_start, (round(game_start.get_width()*(WIDTH / 1920) / 2), round(game_start.get_height()*(HEIGHT / 1080) / 2)))
                                                         
        self.game_start_button = pygame.transform.smoothscale(game_start_button, (round(game_start_button.get_width()*(WIDTH / 1920) / 2.2), round(game_start_button.get_height() * (HEIGHT / 1080) / 2.2)))

        self.rules = pygame.transform.smoothscale(rules, (round(rules.get_width() * (WIDTH / 1920) / 3), round(rules.get_height() * (HEIGHT / 1080) / 3)))

        self.rules_2 = pygame.transform.smoothscale(rules, (round(rules.get_width() * (WIDTH / 1920)), round(rules.get_height() * (HEIGHT / 1080))))
        
        self.exit = pygame.transform.smoothscale(exit, (round(exit.get_width() * (WIDTH / 1920) / 2), round(exit.get_height() * (HEIGHT / 1080) / 2)))

        self.rules_button = pygame.transform.smoothscale(rules_button, (round(rules_button.get_width() * (WIDTH / 1920) * 1.6), round(rules_button.get_height() * (HEIGHT / 1080) * 1.6)))

        self.rules_zones = pygame.transform.smoothscale(rules_zones, (round(rules_zones.get_width() * (WIDTH / 1920) / 2), round(rules_zones.get_height() * (HEIGHT/ 1080) / 2)))

        self.rules_zones_2 = pygame.transform.smoothscale(rules_zones_2, (round(rules_zones_2.get_width() * (WIDTH / 1920) / 2), round(rules_zones_2.get_height() * (HEIGHT / 1080) / 2)))

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
        self.place_for_text.fill(BLACK)
        self.screen.blit(self.place_for_text, (round(WIDTH * 0.24), round(HEIGHT * 0.04)))
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
        text_sea = f2.render('Вода', True, (255, 255, 255))
        text_mountains = f2.render('Горы', True, (255, 255, 255))
        text_forest = f2.render('Лес', True, (255, 255, 255))
        text_desert = f2.render('Пустыня', True, (255, 255, 255))
        text_huts = f2.render('Хижины', True, WHITE)
        text_monuments = f2.render('Монументы', True, WHITE)
        text_jaguars_1 = f2.render('Поля c', True, WHITE)
        text_jaguars_2 = f2.render('ягуарами', True, WHITE)
        text_bears = f2.render('медведями', True, WHITE)
        self.screen.blit(self.exit, (round(0.99*WIDTH - self.exit.get_width()), round(0.01 * HEIGHT)))
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
        self.screen.fill(BLACK)
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

    def draw_false_answer(self):
        self.place_for_text.fill(BLACK)
        text_false_answer = f1.render('Ошибка! Вопрос не может быть задан самому себе.', True, WHITE)
        self.place_for_text.blit(text_false_answer, (0, 0))
        self.screen.blit(self.place_for_text, (round(0.24*WIDTH), round(0.04*HEIGHT)))
        pygame.display.update()

    def draw_false_input(self):
        self.place_for_text.fill(BLACK)
        text_false_input = f1.render('Ошибка! Попытка дать ответ, не соответствующий подсказке.', True, WHITE)
        self.place_for_text.blit(text_false_input, (0,0))
        self.screen.blit(self.place_for_text, (round(0.24*WIDTH), round(0.04*HEIGHT)))
        pygame.display.update()

    def draw_greeting_screen(self):
        '''отрисовка приветственного экрана с краткими правилами игры, с надписью 'выберите количество игроков' и тремя
         кнопками : 3, 4 и 5, и кнопкой 'продолжить' '''
        self.screen.fill(BLACK)
        self.screen.blit(self.exit, (round(0.99*WIDTH - self.exit.get_width()), round(0.01 * HEIGHT)))
        text_heading = f1.render('Настольная игра криптид', True,
                                 (255, 255, 255))
        self.screen.blit(text_heading, (round(0.4*WIDTH), round(0.2*HEIGHT)))
        self.screen.blit(self.cryptid_text, (round(WIDTH*0.15), round(HEIGHT*0.08)))
        self.screen.blit(self.image_of_cryptid_1,(round(WIDTH - self.image_of_cryptid_1.get_width()), round(0.2*HEIGHT)))
        self.screen.blit(self.image_of_cryptid_2, (round(0*WIDTH), round(HEIGHT - self.image_of_cryptid_2.get_height())))
        self.screen.blit(self.rules, (round(0.35*WIDTH), round(self.cryptid_text.get_height() + 0.1*HEIGHT)))
        self.screen.blit(self.rules_button, (round(0.35*WIDTH), round(0.6*HEIGHT)))
        self.screen.blit(self.game_start, (round(0.55*WIDTH), round(self.cryptid_text.get_height() + 0.1*HEIGHT)))
        self.screen.blit(self.game_start_button, (round(0.53*WIDTH), round(0.57*HEIGHT)))
        pygame.display.update()
    
    def draw_rules_screen(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.rules, (0.01 * WIDTH, 0))
        self.screen.blit(self.exit, (round(0.99*WIDTH - self.exit.get_width()), round(0.01 * HEIGHT)))
        text_of_rules_1 = f2.render('Игровое поле состоит из шестиугольников. Каждый из них может быть определенного типа:', True, WHITE)
        self.screen.blit(text_of_rules_1, (0.01 * WIDTH, 0.07*HEIGHT))
        self.screen.blit(self.rules_zones, (0.15 * WIDTH, 0.09*HEIGHT))
        text_of_rules_2 = f2.render('Также на шестиугольниках могут располагаться монументы или хижины различных цветов,', True, WHITE)
        text_of_rules_3 = f2.render('шестиугольники, которые снабжены контуром коричневого или орнажевого цветов, являются', True, WHITE)
        text_of_rules_4 = f2.render('местом обитания медведей или ягуаров:', True, WHITE)
        self.screen.blit(text_of_rules_2, (0.01 * WIDTH, 0.23*HEIGHT))
        self.screen.blit(text_of_rules_3, (0.01 * WIDTH, 0.26*HEIGHT))
        self.screen.blit(text_of_rules_4, (0.01 * WIDTH, 0.29*HEIGHT))
        self.screen.blit(self.rules_zones_2, (0.15 * WIDTH, 0.32 * HEIGHT))
        text_array= []
        text_array.append(f2.render('       В начале игры каждый из игроков получает подсказку в которой содержится  информация', True, WHITE))
        text_array.append(f2.render('о местонахождении криптида. Пример подсказки: криптид может находится или в воде или в горах.', True, WHITE))
        text_array.append(f2.render('Или так: Криптид находиться не дальше двух клеток от синего сооружения. Зная информацию из', True, WHITE))
        text_array.append(f2.render('трёх подсказок можно одназночно узнать местоположение криптида. В начале игроки по очереди', True, WHITE))
        text_array.append(f2.render('ставят квадратики на те клетки, где согласно их подсказке не может находится криптид. Для этого', True, WHITE)) 
        text_array.append(f2.render('необходимо нажать ЛКМ на соответствующую из клеток. Каждый должен поставить по два квадратика.', True, WHITE))
        text_array.append(f2.render('       Далее начинается основной ход игры. Игроки по очереди задают друг другу вопросы о местонахождении ', True, WHITE))
        text_array.append(f2.render('криптида, для этого необходимо нажать ЛКМ на ту клетку, о которой вы хотите узнать информацию от другого игрока,', True, WHITE))
        text_array.append(f2.render('и его номер на клавиатуре 2 или 3, если вы игрок 1. Если согласно подскаске игрока в этой клетке может', True, WHITE))
        text_array.append(f2.render('быть криптид будет нарисован круг, в противном случае квадрат. Если был нарисован квадрат, то вы тоже', True, WHITE))
        text_array.append(f2.render('должны отметить, где не может находиться криптид, для этого нажмите ЛКМ на соответствующую клетку.', True, WHITE))
        i = 0
        for texts in text_array:
            self.screen.blit(texts, (0.01 * WIDTH, (0.49 + i) * HEIGHT))
            i += 0.03
        pygame.display.update()
    #def draw_hint_screen(self, hints):
        #for hint in hints:
        #    if hint.type == BuildingTypeHint
        #self.screen.fill(BLACK)
        #text_of_hint_1 = 
        #text_of_hint_2 = 
        #text_of_hint_3 = 
        pass
    def exit_button(self, coords:coordinates):
        x = coords[0]
        y = coords[1]
        if (x >= round(0.99*WIDTH - self.exit.get_width())) and (y <= round(self.exit.get_height())):
            return True
        else:
            return False
    def to_rules_button_start_screen(self, coords:coordinates):
        x = coords[0]
        y = coords[1]
        if (x >= round(0.35*WIDTH)) and (x <= round(0.35*WIDTH + self.rules_button.get_width())) and (y >= round(0.6*HEIGHT)) and (y <= round(0.6*HEIGHT + self.rules_button.get_height())):
            return True
        else:
            return False
    def to_game_button(self, coords:coordinates):
        x = coords[0]
        y = coords[1]
        print(x, y)
        print(round(0.53*WIDTH), round(0.53 * WIDTH + self.game_start_button.get_width()), round(0.57*HEIGHT), round(0.57*HEIGHT + self.game_start_button.get_height()))
        if (x >= round(0.53*WIDTH)) and (x <= round(0.53 * WIDTH + self.game_start_button.get_width())) and (y >= round(0.57*HEIGHT)) and (y <= round(0.57*HEIGHT + self.game_start_button.get_height())):
            return True
        else:
            return False
    def choose_number_of_players_button(self, coords: coordinates):
        '''обработка нажатия на кнопки с количеством игроков на приветственном экране. возвращает None, если координаты
        не попадают ни в одну из кнопок, а если попадают, то возвражает число, написанное на кнопке (3, 4 или 5)'''
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








