from enum import Enum

coordinates = tuple[int, int]

class Color(Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

class Zone(Enum):
    SWAMP = 'swamp'
    DESERT = 'desert'
    MOUNTAINS = 'mountains'
    FOREST = 'forest'
    WATER = 'water'
    NONE = None

class BuildingType(Enum):
    HUT = 'hut'
    MONUMENT = 'monument'
    NONE = None

class Animal(Enum):
    BEAR = 'bear'
    JAGUAR = 'jaguar'
    NONE = None


Building = tuple[BuildingType, Color] | None

