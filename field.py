from dataclasses import dataclass
from abc import ABC, abstractmethod

from custom_types import coordinates, Building, Zone

@dataclass(frozen=True)
class Hex:

    zone: str
    animal: str
    building: str
    circles: list[str]
    squares: list[str]


    
class Hint(ABC):
    @abstractmethod
    def check(self, cell: coordinates, field: dict[coordinates, Hex]) -> bool:
        pass
    

@dataclass
class BuildingHint(Hint):
    distance: int
    building: Building
    
    def check(self, cell: coordinates, field: dict[coordinates, Hex]) -> bool:
        return ...
    

@dataclass
class SingleZoneHint(Hint):
    zone: Zone

    def check(self, cell: coordinates, field: dict[coordinates, Hex]) -> bool:
        return ...


class Field:
    def __init__(self, hex: dict[coordinates, Hex]):
        """ hex - словарь из клеток в формате: {(x, y): [zone, animals, building]} """
        self.hex = {}
        
        for coords in hex.keys():
            self.hex[coords] = Hex(*hex[coords])

        """ self.hex - словарь из объектов класса Hex в формате: {(x, y): Hex((x, y), zone, animals, building)}"""

    def calculate_distance(self, coords_1: list[...], coords_2: list[...]):
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
        pass