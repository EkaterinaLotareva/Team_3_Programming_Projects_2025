import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
canvas = pygame.Surface((800, 600))  # Дополнительный слой для рисования
canvas.fill((0, 0, 0))  # Начальный фон
background_color = (0, 0, 0)

running = True
drawing = False
f1 = pygame.font.Font(None, 36)
text1 = f1.render('Hello Привет', True,
                  (255, 255, 255))
canvas.blit(text1, (300, 500))
pygame.display.update()
while running:
    screen.blit(text1, (300, 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            # Рисуем линию при движении мыши
            pygame.draw.circle(canvas, (255, 255, 255), event.pos, 5)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Очистка холста
                canvas.fill(background_color)

    # Отображаем холст на экране
    screen.blit(canvas, (0, 0))
    pygame.display.flip()

pygame.quit()