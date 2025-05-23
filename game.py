import pygame

from view import View
from field import *
from config import *
from custom_types import coordinates, Color

class Game:
    def __init__(self, screen, hex: dict[coordinates: Hex], hints):       #количество игроков пока 3
        self.field = Field(hex)
        self.screen = screen
        self.turn = 0
        self.view = View(self.field, self.screen)
        self.clock = pygame.time.Clock()
        self.mouse_click_pixel = (0, 0)
        self.mouse_click_logic = (0, 0)
        self.player_asked = 0
        self.status = {'finished': False, 'turn_ended': False, 'game_ended': False, 'winner': 0}
        self.colors = [Color.RED, Color.GREEN, Color.BLUE]
        self.hints = []
        self.kriptid = ()

        for i, hint in enumerate(hints):
        # for hint in hint:
            # match hint[0]:
            #     case 'building color':
            #         self.hints.append(BuildingColorHint(hint[1], self.field, hint[2]))
            #     case '...':
            #         ...
            
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

    def answer(self, hex: coordinates, player: int):
        if self.hints[player].check(hex):
            self.view.draw_circle(hex, self.colors[player])
        else:
            self.view.draw_square(hex, self.colors[player])

    #def kriptid(self):
    
    def process_place_square(self, event):
        if event.type == pygame.QUIT:
            self.status['finished'] = True
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.mouse_click_pixel = (event.pos[0], event.pos[1])
            self.view.draw_square(self.view.from_pixels_to_logic(self.mouse_click_pixel), self.colors[player])
            return True
        return False

    def place_square(self, player: int):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status['finished'] = True
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_click_pixel = (event.pos[0], event.pos[1])
                self.view.draw_square(self.view.from_pixels_to_logic(self.mouse_click_pixel), self.colors[player])

    def processing_mouse_click(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status['finished'] = True
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_click_pixel = (event.pos[0], event.pos[1])
                self.mouse_click_logic = self.view.from_pixels_to_logic

    def process_number_key(self, event):
        if event.type == pygame.QUIT:
            self.status['finished'] = True
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.player_asked = 0
                return True
            elif event.key == pygame.K_2:
                self.player_asked = 1
                return True
            elif event.key == pygame.K_3:
                self.player_asked = 2
                return True
        return False            

    def processing_number_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status['finished'] = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.player_asked = 0
                elif event.key == pygame.K_2:
                    self.player_asked = 1
                elif event.key == pygame.K_3:
                    self.player_asked = 2

    def question(self):
        events = pygame.event.get()
        for event in events:
            if self.process_place_square(event):
                continue
            if self.process_number_key(event):
                continue
        # self.processing_mouse_click()
        # self.processing_number_key()

    def find(self):
        self.status['game_ended'] = True
        self.processing_mouse_click()
        for i in range(3):
            self.answer(self.mouse_click_logic, i)
        for i in range(3):
            if not self.hints[i].check(self.mouse_click_logic):
                self.status['game_ended'] = False

    def check_find(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status['finished'] = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

    def run(self):
        self.view.draw_field(self.field)

        while self.turn <= 5:
            self.place_square(self.turn % 3)
            self.turn += 1






