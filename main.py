import pygame
import game
import config
import base_of_fields
pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.FULLSCREEN)
g = game.Game(screen, base_of_fields.hex3, base_of_fields.hints3_3)
g.run()



