import time

import pygame
from view import View
from field import *
from config import *
from custom_types import coordinates, Zone, Animal, Building, Color

class Game:
    def __init__(self, screen, hex: dict[coordinates: [Hex]], hints):       #количество игроков пока 3
        self.field = Field(hex)
        self.screen = screen
        self.turn = 0
        self.view = View(self.field, self.screen)
        self.mouse_click_pixel = (0, 0)
        self.mouse_click_logic = None
        self.player_asked = None
        self.search = None
        self.status = {'running': True, 'start_stage': True, 'turn_ended': False, 'game_ended': False, 'winner': 0, }
        self.colors = [RED, GREEN, BLUE]
        self.hints = []
        self.kriptid = ()
        self.players = 3

        for i, hint in enumerate(hints):
            match hint[0]:
                case 'building color':
                    self.hints.append(BuildingColorHint(hint[1], self.field, hint[2]))
                case 'building type':
                    self.hints.append(BuildingTypeHint(hints[i][1], self.field, hints[i][2]))
                case 'animal':
                    self.hints.append(AnimalHint(hints[i][1], self.field, hints[i][2]))
                case 'two zones':
                    self.hints.append(IntoZonesHint(hints[i][1], self.field))
                case 'zone':
                    self.hints.append(SingleZoneHint(hints[i][1], self.field, hints[i][2]))


    def answer(self, hex: coordinates, player: int):

        if self.hints[player].check(hex):
            self.view.draw_circle(self.mouse_click_pixel, self.colors[player])
            self.field.add_circles(hex, player)
        else:
            self.view.draw_square(self.mouse_click_pixel, self.colors[player])
            self.field.add_squares(hex, player)
            while not self.process_place_square():
                time.sleep(0.1)
        self.turn += 1
        self.view.draw_turn((self.turn % self.players) + 1)

    def process_place_square(self):
        print('inside')
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('action')
                self.mouse_click_pixel = (event.pos[0], event.pos[1])
                logic_coords = self.view.from_pixels_to_logic(self.mouse_click_pixel)
                if not self.hints[self.turn % self.players].check(logic_coords):
                    if not logic_coords == (-10, -10):
                        self.view.draw_square(self.mouse_click_pixel, self.colors[self.turn % self.players])
                        self.field.add_squares(logic_coords, self.turn % self.players)
                        return True
                else:
                    self.view.draw_false_input()


    def process_mouse_click(self, event):

        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.mouse_click_pixel = (event.pos[0], event.pos[1])
            self.mouse_click_logic = self.view.from_pixels_to_logic(self.mouse_click_pixel)
            return True

    def process_number_key(self, event):

        if event.type == pygame.QUIT:
            pygame.quit()

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


    def question(self):

        for event in pygame.event.get():
            self.process_mouse_click(event)
            self.process_number_key(event)
            if (self.mouse_click_logic != None) and self.check_find(event):
                self.find()
                break
        if (self.mouse_click_logic != None) and (self.player_asked != None):
            if self.player_asked != self.turn % self.players:
                self.answer(self.mouse_click_logic, self.player_asked)
                self.mouse_click_logic = None
                self.player_asked = None
            else:
                self.view.draw_false_answer()
                '''написать что нельзя задать вопрос самому себе'''

    def find(self):
        self.status['game_ended'] = True
        for i in range(self.players):
            self.answer(self.mouse_click_logic, i)
        for i in range(self.players):
            if not self.hints[i].check(self.mouse_click_logic):
                self.status['game_ended'] = False

    def check_find(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return True

    def final_stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def run(self):
        self.view.greeting_screen()
        self.view.draw_field()

        while self.status['running']:
            while not self.status['game_ended']:
                if self.status['game_ended']:
                    break
                if self.status['start_stage']:
                    while self.turn < self.players * 2:
                        if self.process_place_square():
                            self.turn += 1
                            print((self.turn + 1) % self.players + 1)
                            self.view.draw_turn((self.turn % self.players) + 1)
                        time.sleep(0.1)
                    self.status['start_stage'] = False
                else:
                    self.question()
            self.final_stage()


        print('игра окончена')











