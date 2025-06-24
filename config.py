import math

ROWS, COLS = 9, 12
WIDTH, HEIGHT = 1200, 700

hex_height = HEIGHT / (ROWS * 3/4 + 1/4)  #высота гекса
hex_radius = hex_height/2   #радиус гекса
hex_width = hex_radius * 2 / math.sqrt(3)  #ширина гекса

radius = (WIDTH + HEIGHT) // 60 # размер шестиугольника
offset_x_1 = WIDTH // 2.7
offset_y_1 = HEIGHT // 1.3

offset_x = (WIDTH - (COLS - 1)*hex_width * 3/4 - hex_width)//2
offset_y = (HEIGHT - (ROWS - 1)* hex_height * 3/4 - hex_height)//2


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)
WHITE = (255, 255, 255)
ORANGE = (251, 139, 35)