from enum import Enum

coordinates = tuple[int, int]

class Color(Enum):
    WHITE = 'white'
    GREEN = 'green'
    BLUE = 'blue'

class Zone(Enum):
    SWAMP = 'swamp'
    DESERT = 'desert'
    MOUNTAINS = 'mountains'
    FOREST = 'forest'
    WATER = 'water'

class BuildingType(Enum):
    HUT = 'hut'
    MONUMENT = 'monument'

class Animal(Enum):
    BEAR = 'bear'
    JAGUAR = 'jaguar'


Building = tuple[BuildingType, Color]

