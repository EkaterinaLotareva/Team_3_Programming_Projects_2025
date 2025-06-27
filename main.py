import pygame
import game
import config
import base_of_fields
pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.FULLSCREEN)
g = game.Game(screen, base_of_fields.hex1, base_of_fields.hints1_3)
g.run()



