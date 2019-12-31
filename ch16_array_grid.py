import pygame

# Colour presets
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

# Parameters
SCREEN = 255, 255
WIDTH = 20
HEIGHT = 20
MARGIN = 5
FPS = 60


def get_rect_surface(width, height, colour):
    s = pygame.Surface((width, height))
    s.fill(colour)
    return s


def game():
    # Initialise, create display, initialise clock
    pygame.init()

    screen = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("array-backed grid")
    font = pygame.font.SysFont("arial", 14)

    clock = pygame.time.Clock()

    # Program initialisation, first frame logic
    grid = [[0 for _ in range(10)] for _ in range(10)]

    screen.fill(BLACK)
    pygame.display.flip()

    # Program loop
    done = False
    while not done:
        # Game logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (HEIGHT + MARGIN)
                column = x // (WIDTH + MARGIN)
                row_remainder = y % (HEIGHT + MARGIN)
                column_remainder = x % (WIDTH + MARGIN)
                if row < len(grid) and row_remainder >= MARGIN:
                    if column < len(grid[0]) and column_remainder >= MARGIN:
                        grid[row][column] = not grid[row][column]

        # Draw game elements
        for column in range(10):
            x = column * (WIDTH + MARGIN) + MARGIN
            for row in range(10):
                y = row * (HEIGHT + MARGIN) + MARGIN
                colour = WHITE
                if grid[row][column]:
                    colour = GREEN
                screen.blit(get_rect_surface(WIDTH, HEIGHT, colour), (x, y))

        # Update display
        pygame.display.flip()  # Update only rects modified in this frame

        # Limit framerate
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    game()
