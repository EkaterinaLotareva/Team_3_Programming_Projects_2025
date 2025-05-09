from enum import Enum

coordinates = tuple[int, int]


class Color(Enum):
    BLACK = 'black'
    WHITE = 'white'
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    

class Zone(Enum):
    SWAMP = 'swamp'
    

class BuildingType(Enum):
    HUT = 'hut'
    MONUMENT = 'monument'
    

class Animal(Enum):
    pass
    
    
Building = tuple[BuildingType, Color]
