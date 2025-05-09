from dataclasses import dataclass
from abc import ABC, abstractmethod

from custom_types import coordinates, Building, Zone, Animal, BuildingType, Color

@dataclass
class Hex:
    zone: Zone
    animal: Animal
    building: Building

    def __init__(self, zone, animal, building):
        self.zone = zone
        self.animal = animal
        self.building = building
        self.circles = []
        self.squares = []


class Field:
    def __init__(self, hex: dict[coordinates, [Zone, Animal, Building]]):
        self.hex = {}

        for coords in hex.keys():
            self.hex[coords] = Hex(*hex[coords])

        """ self.hex - словарь из объектов класса Hex в формате: {(x, y): Hex(zone, animal, building)}"""

    def add_circles(self, coords: coordinates, player):
        self.hex[coords].circles.append(player)

    def add_squares(self, coords: coordinates, player):
        self.hex[coords].squares.append(player)


class Hint(ABC):
    def calculate_distance(self, coords_1: coordinates, coords_2: coordinates):
        x1 = coords_1[0]
        y1 = coords_1[1]
        x2 = coords_2[0]
        y2 = coords_2[1]
        z1 = -x1 - y1
        z2 = -x2 - y2
        return (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))/2
    @abstractmethod
    def check(self, hex: coordinates) -> bool:
        pass
    

class BuildingTypeHint(Hint):
    distance: int
    building_type: BuildingType
    field: Field

    def __init__(self, building_type, field, distance):
        self.building_type = building_type
        self.field = field
        self.distance = distance
    
    def check(self, hex: coordinates) -> bool:
        for coords in self.field.hex.keys():
            if self.calculate_distance(hex, coords) <= self.distance:
                if self.field.hex[coords].building[0] == self.building_type:
                    return True
        return False
    
class BuildingColorHint(Hint):
    distance: int
    color: Color
    field: Field

    def __init__(self, color, field, distance):
        self.color = color
        self.field = field
        self.distance = distance

    def check(self, hex: coordinates) -> bool:
        for coords in self.field.hex.keys():
            if self.calculate_distance(hex, coords) <= self.distance:
                if self.field.hex[coords].building[1] == self.color:
                    return True
        return False


class AnimalHint(Hint):
    distance: int
    animal: Animal
    field: Field

    def __init__(self, animal, field, distance):
        self.animal = animal
        self.field = field
        self.distance = distance

    def check(self, hex: coordinates) -> bool:
        for coords in self.field.hex.keys():
            if self.calculate_distance(hex, coords) <= self.distance:
                if self.field.hex[coords].animal == self.animal:
                    return True
        return False

class SingleZoneHint(Hint):
    distance: int
    zone: Zone
    field: Field
    def __init__(self, zone, field, distance):
        self.zone = zone
        self.field = field
        self.distance = distance
    def check(self, hex: coordinates) -> bool:
        for coords in self.field.hex.keys():
            if self.calculate_distance(hex, coords) <= self.distance:
                if self.field.hex[coords].zone == self.zone:
                    return True
        return False


class IntoZonesHint(Hint):
    zones: [Zone, Zone]
    field: Field
    def __init__(self, zones, field):
        self.zones = zones
        self.field = field
    def check(self, hex: coordinates) -> bool:
        if self.field.hex[hex].zone == self.zones[0] or self.field.hex[hex].zone == self.zones[1]:
            return True
        else:
            return False