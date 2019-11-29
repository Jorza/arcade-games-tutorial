import pygame
from math import pi

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

pygame.init()

size = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    screen.lock()
    # rect tests
    top_corner = 55, 30
    pygame.draw.rect(screen, RED, (top_corner[0], top_corner[1], 200, 25))
    for offset in range(50, 446, 50):
        pygame.draw.rect(screen, GREEN, (top_corner[0] + offset, top_corner[1] + offset/2, 200, 25), 3)
    pygame.draw.rect(screen, BLUE, (0, 0, 40, 40), 20)
    pygame.draw.rect(screen, BLUE, (-20, 200, 40, 40), 20)

    # lines, aalines, polygon
    line_points = (50, 180), (50, 300), (300, 300), (200, 280), (240, 210)
    pygame.draw.lines(screen, BLACK, True, line_points, 20)
    pygame.draw.lines(screen, BLACK, True, [(x + 300, y) for x, y in line_points], 20)
    pygame.draw.aalines(screen, BLACK, True, [(x, y + 150) for x, y in line_points], 0)
    pygame.draw.aalines(screen, BLACK, True, [(x + 300, y + 150) for x, y in line_points])
    pygame.draw.polygon(screen, BLACK, [(x, y + 300) for x, y in line_points], 20)
    pygame.draw.polygon(screen, BLACK, [(x + 300, y + 300) for x, y in line_points], 2)

    # circle, ellipse, arc
    rect = 750, 30, 350, 500
    pygame.draw.arc(screen, GREEN, rect, 0, pi, 10)
    pygame.draw.arc(screen, BLUE, rect, pi, 0, 2)
    pygame.draw.arc(screen, GREEN, rect, 7*pi/6, 3*pi/2, 2)
    screen.unlock()

    # text
    strings = ("This is a rect", "This is a polygon", "These are arcs")
    positions = ((155, 30), (175, 530), (925, 255))
    texts = (
        font.render(strings[0], True, BLACK),
        font.render(strings[1], True, WHITE, BLACK),
        font.render(strings[2], False, GREEN)
    )
    for i in range(len(texts)):
        screen.blit(texts[i], positions[i])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
