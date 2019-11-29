import pygame

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

# Initialise, create display, initialise clock
pygame.init()

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")

clock = pygame.time.Clock()

# Program loop
done = False
while not done:
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic

    # Drawing - background
    screen.fill(WHITE)

    # Drawing - elements

    # Update display
    pygame.display.flip()
    # Limit framerate
    clock.tick(60)
pygame.quit()
