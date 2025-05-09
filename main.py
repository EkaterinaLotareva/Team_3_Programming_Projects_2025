import pygame
pygame.init()


screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
pygame.display.set_caption('test')
fps = 60
clock = pygame.time.Clock()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    clock.tick(fps)



