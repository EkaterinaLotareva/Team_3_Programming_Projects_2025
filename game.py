import pygame
import player
import view
import field
from config import test_hex

class Game:
    def __init__ (self, screen):
        self.field = field.Field(test_hex)
        self.screen = screen
        self.players = (player.Player(), player.Player(), player.Player)
        self.turn = 1
        self.view = view.View(self.players, self.turn, self.screen)
        self.clock = pygame.time.Clock()
        self.mouse_holding = (False, (0, 0))
        self.status = {'start_stage': True, 'finished': False, 'turn_ended': False, 'game_ended': False, 'winner': 0}

    def check_hint(self, hint: Hint, cell: Hex):
        return hint.check(cell, self.field.data)

    def run(self):
        pass

    def question(self):
        pass

    def answer(self):
        pass

    def find(self):
        pass

    def check(self):
        pass
