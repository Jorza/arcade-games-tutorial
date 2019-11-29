import pygame
import time
from collections import deque
import random

# Colour presets
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

# Parameters
SCREEN = 700, 500

INIT_SIZE = 40
INIT_VELOCITY = 2
TRAIL_LENGTH = 10
TRAIL_SPACING = 5
COLOUR_LENGTH = 3
MIN_ALPHA = 50
MAX_ALPHA = 255


def blit_with_alpha(surface, rect_object, colour, alpha):
    s = pygame.Surface((rect_object.width, rect_object.height))
    s.fill(colour)
    s.set_alpha(alpha)
    surface.blit(s, rect_object)


def get_random_colour():
    return [random.randint(0, 255) for _ in range(3)]


def init_trail(trail, colour, init_rect):
    rect = init_rect
    for i in range(trail.maxlen):
        trail.append((rect, colour))
        rect = rect.move(-INIT_VELOCITY, -INIT_VELOCITY)


def bouncing_rect():
    # Initialise, create display, initialise clock
    pygame.init()

    screen = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("bouncing rect")
    font = pygame.font.SysFont("arial", 14)

    clock = pygame.time.Clock()

    # Program initialisation, first frame logic
    alpha_modifier = (MAX_ALPHA - MIN_ALPHA) // (TRAIL_LENGTH - 1)
    velocity_x = INIT_VELOCITY
    velocity_y = INIT_VELOCITY
    start_time = time.time()

    rect = pygame.Rect((0, 0, INIT_SIZE, INIT_SIZE))
    colour = get_random_colour()
    colour_counter = 0

    trail = deque([], (TRAIL_LENGTH - 1) * TRAIL_SPACING + 1)
    init_trail(trail, colour, rect)

    # Program loop
    done = False
    while not done:
        # FPS calculator
        try:
            current_fps = int(1/(time.time() - start_time))
        except ZeroDivisionError:
            current_fps = 0
        start_time = time.time()

        # Drawing - background
        screen.fill(BLACK)

        # Drawing - elements
        alpha = MAX_ALPHA - alpha_modifier * (TRAIL_LENGTH - 1)
        for i, (trail_rect, trail_colour) in enumerate(trail):
            if i % TRAIL_SPACING == 0:
                blit_with_alpha(screen, trail_rect, trail_colour, alpha)
                alpha += alpha_modifier

        # Drawing - FPS
        text = font.render("FPS: " + str(current_fps), True, WHITE)
        screen.blit(text, (0, 0))

        # Update display
        pygame.display.flip()

        # Game logic - update for next frame
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Compute new velocities, create next rect.
        if rect.left < 0 or rect.right > SCREEN[0]:
            velocity_x *= -1
        if rect.top < 0 or rect.bottom > SCREEN[1]:
            velocity_y *= -1
        rect = rect.move(velocity_x, velocity_y)
        # Set colour of new rect
        if colour_counter == COLOUR_LENGTH * TRAIL_SPACING:
            colour = get_random_colour()
            colour_counter = 0
        else:
            colour_counter += 1
        # Update trail
        if len(trail) == trail.maxlen:
            trail.popleft()
        trail.append((rect, colour))

        # Limit framerate
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    bouncing_rect()
