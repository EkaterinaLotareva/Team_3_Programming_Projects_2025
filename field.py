class Hex:
    def __init__(self, zone, animal, building):
        """ клетка поля """
        self.zone = zone
        self.animal = animal
        self.building = building
        self.circles = []
        self.squares = []

class Field:
    def __init__(self, hex: dict):
        """ hex - словарь из клеток в формате: {(x, y): [zone, animals, building]} """
        self.hex = {}

        for coords in hex.keys():
            self.hex[coords] = Hex(*hex[coords])

        """ self.hex - словарь из объектов класса Hex в формате: {(x, y): Hex((x, y), zone, animals, building)}"""

    def calculate_distance(self, coords_1, coords_2: list):
        x1 = coords_1[0]
        y1 = coords_1[1]
        x2 = coords_2[0]
        y2 = coords_2[1]
        z1 = -x1 -y1
        z2 = -x2 -y2
        return((abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))/2)

    def add_circles(self, coords, player):
        self.hex[coords].circles.append(player)

    def add_squares(self, coords, player):
        self.hex[coords].squares.append(player)

    def search(self):