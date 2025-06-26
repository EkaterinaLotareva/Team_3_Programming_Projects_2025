import math
import pygame
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
image_of_cryptid_1 = pygame.image.load('images_of_field/Криптид_картинка 1.png').convert_alpha()
        
image_of_cryptid_2 = pygame.image.load('images_of_field/Криптид картинка 2.png').convert_alpha()

cryptid_text = pygame.image.load('images_of_field/Криптид надпись.png').convert_alpha()

game_start = pygame.image.load('images_of_field/Начать игру надпись.png').convert_alpha()

game_start_button = pygame.image.load('images_of_field/Начать игру кнопка.png').convert_alpha()

rules = pygame.image.load('images_of_field/Правила надпись.png').convert_alpha()

rules_button = pygame.image.load('images_of_field/Правила_криптид.png').convert_alpha()

rules_zones = pygame.ima

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