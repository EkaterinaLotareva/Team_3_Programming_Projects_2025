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
        self.status = {'running': True, 'greeting_screen': True, 'hint_screen': False, 'rules_screen': False,
                       'start_stage': False, 'main_stage': False, 'turn_ended': False, 'game_ended': False, 'winner': 0,
                       'from_greeting': False, 'from_start': False, 'from_main': False}
        self.colors = [RED, GREEN, BLUE]
        self.hints = []
        self.kriptid = ()
        self.players = 3
        self.player_hint_screen = -1
        self.need_square = False

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
            self.field.add_circles(hex, self.mouse_click_pixel, self.colors[player])
        else:
            self.view.draw_square(self.mouse_click_pixel, self.colors[player])
            self.field.add_squares(hex, self.mouse_click_pixel, self.colors[player])
            return False
        self.turn += 1
        self.view.draw_turn((self.turn % self.players) + 1)
        return True
    def process_place_square(self):
        if self.view.exit_button(self.mouse_click_pixel):
            pygame.quit()
        else:
            logic_coords = self.view.from_pixels_to_logic(self.mouse_click_pixel)
            if not self.hints[self.turn % self.players].check(logic_coords):
                if not logic_coords == (-10, -10):
                    self.view.draw_square(self.mouse_click_pixel, self.colors[self.turn % self.players])
                    self.field.add_squares(logic_coords, self.mouse_click_pixel, self.colors[self.turn % self.players])
                    return True
            else:
                self.view.draw_false_input()
                return False

    def process_mouse_click(self, event):

        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.mouse_click_pixel = (event.pos[0], event.pos[1])
            if self.view.exit_button(self.mouse_click_pixel):
                pygame.quit()
            else:
                self.mouse_click_logic = self.view.from_pixels_to_logic(self.mouse_click_pixel)
            return True

    def question(self):
        if ((self.player_asked) != (self.turn % self.players)) and (self.player_asked != None):
            if self.answer(self.mouse_click_logic, self.player_asked):
                #self.mouse_click_logic = None
                self.mouse_click_pixel = None
                self.player_asked = None
            else:
                self.need_square = True
        else:
            self.view.draw_false_answer()

    def find(self):
        self.status['game_ended'] = True
        for i in range(self.players):
            self.answer(self.mouse_click_logic, i)
        for i in range(self.players):
            if not self.hints[i].check(self.mouse_click_logic):
                self.status['game_ended'] = False
            else:
                self.status['winner'] = self.turn % self.players + 1
                print('WInner')


    def run(self):

        while self.status['running']:
            while not self.status['game_ended']:
                if self.status['greeting_screen']:
                    #print('greeting_screen')
                    self.view.draw_greeting_screen()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.mouse_click_pixel = (event.pos[0], event.pos[1])
                            if self.view.exit_button(self.mouse_click_pixel):
                                pygame.quit()
                            elif self.view.to_rules_button_start_screen(self.mouse_click_pixel):
                                self.status['greeting_screen'] = False
                                self.status['rules_screen'] = True
                                self.status['from_greeting'] = True
                                self.status['from_start'] = False
                                self.status['from_main'] = False
                                self.view.draw_rules_screen()
                            elif self.view.to_game_button(self.mouse_click_pixel):
                                self.status['greeting_screen'] = False
                                self.status['hint_screen'] = True
                                self.status['from_start'] = True
                                self.status['from_greeting'] = False
                                self.status['from_main'] = False
                                self.view.draw_hint_screen(self.hints, self.player_hint_screen)
                elif self.status['rules_screen']:
                    #print('rules_screen')
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.mouse_click_pixel = (event.pos[0], event.pos[1])
                            if self.view.exit_button(self.mouse_click_pixel):
                                pygame.quit()
                            if self.view.back_button_rules(self.mouse_click_pixel):
                                self.status['rules_screen'] = False
                                if self.status['from_start']:
                                    self.status['start_stage'] = True
                                    self.view.draw_field(self.turn % self.players + 1)
                                if self.status['from_greeting']:
                                    self.status['greeting_screen'] = True
                                    self.view.draw_greeting_screen()
                                if self.status['from_main']:
                                    self.status['main_stage'] = True
                                    self.view.draw_field(self.turn % self.players + 1)
                elif self.status['hint_screen']:
                    #print('hint_screen')
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.mouse_click_pixel = (event.pos[0], event.pos[1])
                            if self.view.exit_button(self.mouse_click_pixel):
                                pygame.quit()
                            if self.view.hint_button(self.mouse_click_pixel) != False:
                                if self.player_hint_screen == -1:
                                    self.player_hint_screen = self.view.hint_button(self.mouse_click_pixel)
                                    self.view.draw_hint_screen(self.hints, self.player_hint_screen)
                                else:
                                    self.player_hint_screen = -1
                                    self.view.draw_hint_screen(self.hints, self.player_hint_screen)
                            if self.view.back_button_hints(self.mouse_click_pixel):
                                self.status['hint_screen'] = False
                                self.player_hint_screen = -1
                                if self.status['from_start']:
                                    self.status['start_stage'] = True
                                    self.view.draw_field(self.turn % self.players + 1)
                                if self.status['from_main']:
                                    self.status['main_stage'] = True
                                    self.view.draw_field(self.turn % self.players + 1)
                elif self.status['start_stage']:
                    #print('start_stage')
                    while self.turn < self.players * 2:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mouse_click_pixel = (event.pos[0], event.pos[1])
                                if self.process_place_square():
                                    self.turn += 1
                                    self.view.draw_turn((self.turn % self.players) + 1)
                                if self.view.exit_button(self.mouse_click_pixel):
                                    pygame.quit()
                                if self.view.to_rules_button_main_screen(self.mouse_click_pixel):
                                    self.status['start_stage'] = False
                                    self.status['rules_screen'] = True
                                    self.status['from_start'] = True
                                    self.status['from_main'] = False
                                    self.status['from_greeting'] = False
                                    self.view.draw_rules_screen()
                                if self.view.to_hints_button(self.mouse_click_pixel):
                                    self.status['start_stage'] = False
                                    self.status['hint_screen'] = True
                                    self.status['from_start'] = True
                                    self.status['from_main'] = False
                                    self.status['from_greeting'] = False
                                    self.view.draw_hint_screen(self.hints, self.player_hint_screen)
                    self.status['start_stage'] = False
                    self.status['main_stage'] = True
                elif self.status['main_stage']:
                    #print('main_stage')
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.mouse_click_pixel = (event.pos[0], event.pos[1])
                            self.mouse_click_logic = self.view.from_pixels_to_logic(self.mouse_click_pixel)
                            if self.view.exit_button(self.mouse_click_pixel):
                                pygame.quit()
                            if self.view.to_rules_button_main_screen(self.mouse_click_pixel):
                                self.status['main_stage'] = False
                                self.status['rules_screen'] = True
                                self.status['from_main'] = True
                                self.status['from_greeting'] = False
                                self.status['from_start'] = False
                                self.view.draw_rules_screen()
                            if self.view.to_hints_button(self.mouse_click_pixel):
                                self.status['main_stage'] = False
                                self.status['hint_screen'] = True
                                self.status['from_main'] = True
                                self.status['from_greeting'] = False
                                self.status['from_start'] = False
                                self.view.draw_hint_screen(self.hints, self.player_hint_screen)
                            if self.need_square:
                                if self.process_place_square():
                                    self.turn += 1
                                    self.view.draw_turn((self.turn % self.players) + 1)
                                    self.need_square = False
                        elif event.type == pygame.KEYDOWN and (self.mouse_click_pixel != None):
                            if event.key == pygame.K_1:
                                self.player_asked = 0
                            elif event.key == pygame.K_2:
                                self.player_asked = 1
                            elif event.key == pygame.K_3:
                                self.player_asked = 2
                            elif event.key == pygame.K_SPACE:
                                self.find()
                            self.question()
            for event in pygame.event.get():
                self.view.draw_winner(self.status['winner'])
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mouse_click_pixel = (event.pos[0], event.pos[1])
                    print(self.mouse_click_pixel)
                    if self.view.exit_button(self.mouse_click_pixel):
                        pygame.quit()



        print('игра окончена')





















