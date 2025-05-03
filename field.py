class Hex:
    def __init__(self, coords, zone, animals, buildings):
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

    def add_circles(self):

    def add_squares(self):

    def search(self):