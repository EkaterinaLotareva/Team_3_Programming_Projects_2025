import pygame
from view import View
from field import *
from config import *
from custom_types import coordinates, Zone, Animal, Building

class Game:
    def __init__(self, screen, hex: dict[coordinates: [Zone, Animal, Building]], hints):       #количество игроков пока 3
        self.field = Field(hex)
        self.screen = screen
        self.turn = 1
        self.view = View(self.field, self.screen)
        self.clock = pygame.time.Clock()
        self.mouse_holding = (False, (0, 0))
        self.status = {'start_stage': True, 'finished': False, 'turn_ended': False, 'game_ended': False, 'winner': 0}
        self.colors = [RED, GREEN, BLUE]
        self.hints = []

        for i in range(len(hints)):
            if hints[i][0] == 'building color':
                hints.append(BuildingColorHint(hints[i][1], self.field, hints[i][2]))
            elif hints[i][0] == 'building type':
                hints.append(BuildingTypeHint(hints[i][1], self.field, hints[i][2]))
            elif hints[i][0] == 'animal':
                hints.append(AnimalHint(hints[i][1], self.field, hints[i][2]))
            elif hints[i][0] == 'two zones':
                hints.append(IntoZonesHint(hints[i][1], self.field))
            elif hints[i][0] == 'zone':
                hints.append(SingleZoneHint(hints[i][1], self.field, hints[i][2]))

    def answer(self, hint: Hint, hex: coordinates, player: int):

        if hint.check(hex):
            self.view.draw_circle(hex, self.colors[player])
        else:
            self.view.draw_square(hex, self.colors[player])

    def question(self):
        pass

    def run(self):
        pass


