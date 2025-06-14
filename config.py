import math
test_hex = {(0, 0): ['mountain', 'jaguar', None], (1, 0): ['forest', None, None], (2, 0): ['forest', None, None],
            (3, 0): ['swamp', None, None], (4, 0): ['swamp', None, None], (5, 0): ['mountain', None, None],
            (6, 0): ['mountain', None, None], (0, 1): ['swamp', 'jaguar', None], (0, 2): ['forest', None, None],
            (0, 3): ['forest', None, None], (0, 4): ['forest', None, None], (0, 5): ['water', None, None],
            (0, -1): ['forest', None, None], (1, -1): ['water', None, None], (2, -1): ['swamp', None, None],
            (3, -1): ['swamp', None, None], (4, -1): ['desert', None, None], (5, -1): ['desert', 'bear', None],
            (1, -2): ['water', None, None], (2, -2): ['water', None, None], (3, -2): ['mountain', None, None],
            (4, -2): ['mountain', 'bear', None], (2, -3): ['water', None, ['blue', 'monument']],
            (3, -3): ['mountain', None, None], (-1, 0): ['mountain', None, None], (-1, 1): ['mountain', None, None],
            (-1, 2): ['mountain', None, None], (-1, 3): ['water', None, None], (-1, 4): ['water', None, None],
            (-2, 1): ['mountain', None, None], (-2, 2): ['water', None, ['white', 'hut']], (-2, 3): ['water', None, None],
            (-3, 2): ['water', None, None], (1, 1): ['swamp', 'jaguar', None], (2, 1): ['forest', None, None],
            (3, 1): ['swamp', None, None], (4, 1): ['mountain', None, None], (5, 1): ['mountain', None, None],
            (6, 1): ['water', None, None], (7, 1): ['water', 'jaguar', None], (1, 2): ['swamp', None, None],
            (1, 3): ['forest', None, None], (1, 4): ['water', None, None], (1, 5): ['water', None, None],
            (1, 6): ['swamp', None, None], (2, 2): ['swamp', None, ['green', 'monument']], (3, 2): ['desert', None, None],
            (4, 2): ['desert', None, None], (5, 2): ['mountain', None, None], (6, 2): ['water', None, None],
            (7, 2): ['forest', None, None], (8, 2): ['forest', 'jaguar', None], (2, 3): ['forest', None, None],
            (2, 4): ['water', None, None], (2, 5): ['water', None, None], (2, 6): ['swamp', None, None],
            (2, 7): ['swamp', None, None], (3, 3): ['forest', None, None], (4, 3): ['desert', None, None],
            (5, 3): ['desert', None, None], (6, 3): ['desert', None, None], (7, 3): ['forest', None, None],
            (8, 3): ['mountain', None, None], (9, 3): ['swamp', None, None], (3, 4): ['forest', None, None],
            (3, 5): ['desert', None, None], (3, 6): ['desert', None, None], (3, 7): ['swamp', None, None],
            (3, 8): ['water', 'bear', None], (4, 4): ['forest', None, None], (5, 4): ['desert', None, None],
            (6, 4): ['desert', None, ['green', 'hut']], (7, 4): ['mountain', None, None],
            (8, 4): ['mountain', None, ['white', 'monument']], (9, 4): ['swamp', None, None],
            (10, 4): ['swamp', None, None], (4, 5): ['desert', 'bear', ['blue', 'hut']], (4, 6): ['desert', 'bear', None],
            (4, 7): ['water', None, None], (4, 8): ['water', 'bear', None], (4, 9): ['mountain', 'bear', None],
            (5, 5): ['forest', 'bear', None], (6, 5): ['desert', None, None], (7, 5): ['mountain', None, None],
            (8, 5): ['desert', None, None], (9, 5): ['forest', None, None], (10, 5): ['forest', 'jaguar', None],
            (11, 5): ['swamp', 'jaguar', None], (5, 6): ['desert', None, None], (5, 7): ['water', None, None],
            (5, 8): ['water', None, None], (5, 9): ['mountain', None, None], (5, 10): ['mountain', None, None],
            (6, 6): ['desert', None, None], (7, 6): ['desert', None, None], (8, 6): ['desert', None, None],
            (9, 6): ['forest', None, None], (10, 6): ['forest', 'jaguar', None], (6, 7): ['desert', None, None],
            (6, 8): ['desert', None, None], (6, 9): ['mountain', None, None], (6, 10): ['mountain', None, None],
            (7, 7): ['swamp', None, None], (8, 7): ['forest', None, None], (9, 7): ['forest', None, None],
            (7, 8): ['swamp', None, None], (7, 9): ['swamp', None, None], (8, 8): ['swamp', None, None]}

test_hints = (('building color', 'white', 3), ('two zones', ('swamp', 'desert')), ('zone', 'water', 1))
'''пример для животных: ('animal', 'bear', 2)
   пример для типа строения: ('building type', 'hut', 3)'''



ROWS, COLS = 9, 12
WIDTH, HEIGHT = 1500, 1000

hex_height = HEIGHT / (ROWS * 3/4 + 1/4)  #высота гекса
hex_radius = hex_height/2   #радиус гекса
hex_width = hex_radius * 2 / math.sqrt(3)  #ширина гекса

radius = (WIDTH + HEIGHT) // 60 # размер шестиугольника
offset_x_1 = WIDTH // 2
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