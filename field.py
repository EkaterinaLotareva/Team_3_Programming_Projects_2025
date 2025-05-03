class Hex:
    def __init__(self, coords, zone, animals, buildings):
        """ клетка поля """
        self.coords = coords
        self.zone = zone
        self.animals = animals
        self.buildings = buildings
        self.circles = None
        self.squares = None

class Field:
    def __init__(self, hex: dict, hints):
        """ hex - словарь из клеток в формате: {(x, y): [zone, animals, building]} """
        self.hints = hints
        self.hex = {}

        for coords in hex.keys():
            self.hex[coords] = Hex(coords, *hex[coords])

        """ self.hex - словарь из объектов класса Hex в формате: {(x, y): Hex((x, y), zone, animals, building)}"""

    def calculate_distance(self, coords_1, coords_2: list):
        x1 = coords_1[0]
        y1 = coords_1[1]
        x2 = coords_2[0]
        y2 = coords_2[1]
        z1 = -x1 -y1
        z2 = -x2 -y2
        return((abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))/2)

    def add_circles(self):

    def add_squares(self):

    def search(self):