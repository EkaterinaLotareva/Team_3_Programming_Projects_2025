import pygame
pygame.init()

sc = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
pygame.display.set_caption('test')
fps = 60
clock = pygame.time.Clock()
FIRE = (235, 100, 49)
ICE = (12, 220, 230)
GRASS = (13, 145, 5)
SILVER = (190, 190, 210)
SUN = (230, 250, 100)

pygame.draw.rect(sc, FIRE, (10, 10, 200, 200), 4)
pygame.draw.rect(sc, FIRE, (200, 250, 90, 80))
pygame.draw.line(sc, ICE, (50, 30), (350, 100), 5)
pygame.draw.lines(sc, GRASS, True, [(6, 90), (180, 112), (44, 230), (234, 289)], 8)
pygame.draw.polygon(sc, SILVER, [(100, 320), (150, 270), (300, 369)])
pygame.draw.circle(sc, SUN, (300, 180), 30)
pygame.display.update()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    clock.tick(fps)



