from enum import Enum

coordinates = tuple[int, int]

class Color(Enum):
    WHITE = 'white'
    GREEN = 'green'
    BLUE = 'blue'
    NONE = None

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


Building = tuple[Color, BuildingType] or None

