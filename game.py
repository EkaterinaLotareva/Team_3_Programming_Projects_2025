import pygame
from view import View
from field import *
from config import *
from custom_types import coordinates, Zone, Animal, Building

class Game:
    def __init__(self, screen, hex: dict[coordinates: [Zone, Animal, Building]], hints):       #количество игроков пока 3
        self.field = Field(hex)
        self.screen = screen
        self.turn = 0
        self.view = View(self.field, self.screen)
        self.clock = pygame.time.Clock()
        self.mouse_click_pixel = (0, 0)
        self.mouse_click_logic = (0, 0)
        self.player_asked = 0
        self.status = {'finished': False, 'turn_ended': False, 'game_ended': False, 'winner': 0}
        self.colors = [RED, GREEN, BLUE]
        self.hints = []
        self.kriptid = ()

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

    def answer(self, hex: coordinates, player: int):

        if self.hints[player].check(hex):
            self.view.draw_circle(hex, self.colors[player])
        else:
            self.view.draw_square(hex, self.colors[player])

    #def kriptid(self):

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
            self.processing_mouse_click()
            self.processing_number_key()

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






