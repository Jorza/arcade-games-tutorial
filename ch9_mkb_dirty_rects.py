"""
Move a character around a 2D canvas, painting where it goes.
Controlled by arrow keys, mouse, or joystick hat (if joystick is connected)
"""

import pygame
import time
import math

# Colour presets
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

# Parameters
SCREEN = 700, 500
FPS = 60
SPEED = 3


def draw_stick_figure(colour):
    s = pygame.Surface((10, 27))
    # Head
    pygame.draw.ellipse(s, WHITE, [1, 0, 10, 10], 0)
    # Legs
    pygame.draw.line(s, WHITE, [5, 17], [10, 27], 2)
    pygame.draw.line(s, WHITE, [5, 17], [0, 27], 2)
    # Body
    pygame.draw.line(s, colour, [5, 17], [5, 7], 2)
    # Arms
    pygame.draw.line(s, colour, [5, 7], [9, 17], 2)
    pygame.draw.line(s, colour, [5, 7], [1, 17], 2)
    return s


def get_keyboard_direction(event):
    if event.key == pygame.K_LEFT:
        return -1, 0
    elif event.key == pygame.K_RIGHT:
        return 1, 0
    elif event.key == pygame.K_UP:
        return 0, -1
    elif event.key == pygame.K_DOWN:
        return 0, 1


def game():
    # Initialise, create display, initialise clock
    pygame.init()
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    screen = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("mouse animation")
    font = pygame.font.SysFont("arial", 14)

    clock = pygame.time.Clock()

    # Program initialisation, first frame logic
    start_time = time.time()
    figure = draw_stick_figure(RED)
    fps_rect = (0, 0, 50, 14)
    current_rect = pygame.Rect((0, 0, figure.get_width(), figure.get_height()))
    direction = [0, 0]

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
            if joystick:
                if event.type == pygame.JOYHATMOTION:
                    if event.hat == 0:
                        direction[0] = event.value[0]
                        direction[1] = -event.value[1]
            else:
                if event.type == pygame.KEYDOWN:
                    key_direction = get_keyboard_direction(event)
                    if key_direction:
                        direction[0] += key_direction[0]
                        direction[1] += key_direction[1]
                elif event.type == pygame.KEYUP:
                    key_direction = get_keyboard_direction(event)
                    if key_direction:
                        direction[0] -= key_direction[0]
                        direction[1] -= key_direction[1]

        x_offset, y_offset = 0, 0
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_offset = mouse_x - current_rect.left
            y_offset = mouse_y - current_rect.top
        else:
            x_offset += direction[0] * SPEED
            y_offset += direction[1] * SPEED
            if abs(direction[0]) + abs(direction[1]) >= 2:
                x_offset /= math.sqrt(2)
                y_offset /= math.sqrt(2)

        previous_rect = current_rect.copy()
        current_rect.move_ip(x_offset, y_offset)

        # Drawing
        pygame.draw.rect(screen, RED, previous_rect)  # Erase figure at old position
        screen.blit(figure, current_rect)  # Draw figure at new position

        pygame.draw.rect(screen, BLACK, fps_rect)
        text = font.render("FPS: " + str(current_fps), True, WHITE)
        screen.blit(text, (0, 0))

        # Update display
        pygame.display.update((previous_rect, current_rect, fps_rect))

        # Limit framerate
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    game()
