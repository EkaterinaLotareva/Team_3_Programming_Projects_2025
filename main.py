import pygame
import game
import config
pygame.init()


screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
g = game.Game(screen, config.test_hex, config.test_hints)
g.run()



