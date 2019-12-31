import pygame
import time

# Colour presets
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

# Parameters
SCREEN = 700, 500
FPS = 60


def game():
    # Initialise, create display, initialise clock
    pygame.init()

    screen = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("array-backed grid")
    font = pygame.font.SysFont("arial", 14)

    clock = pygame.time.Clock()

    # Program initialisation, first frame logic
    start_time = time.time()
    fps_rect = pygame.Rect((0, 0, 50, 16))

    screen.fill(BLACK)
    pygame.display.flip()

    # Program loop
    done = False
    while not done:
        # FPS calculator
        try:
            current_fps = int(1/(time.time() - start_time))
        except ZeroDivisionError:
            current_fps = 0
        start_time = time.time()

        # Game logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Draw game elements

        # Draw FPS display
        pygame.draw.rect(screen, BLACK, fps_rect)
        text = font.render("FPS: " + str(current_fps), True, WHITE)
        screen.blit(text, (fps_rect.x, fps_rect.y))

        # Update display
        pygame.display.flip()  # Update only rects modified in this frame

        # Limit framerate
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    game()
