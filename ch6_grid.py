import pygame

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

pygame.init()

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("grid")

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    screen.lock()
    for x in range(0, 700, 10):
        for y in range(0, 500, 10):
            pygame.draw.rect(screen, GREEN, (x, y, 5, 5))
    screen.unlock()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
