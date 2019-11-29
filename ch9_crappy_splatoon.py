"""
Move a character around a 2D canvas, painting where it goes.
Controlled by arrow keys.
Second player controlled by joystick stick or hat (if connected).
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


class Player:
    @staticmethod
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

    def __init__(self, colour, speed):
        self.colour = colour
        self.figure = self.draw_stick_figure(colour)
        self.direction = [0, 0]  # x-direction, y-direction
        self.speed = speed

        self.current_rect = pygame.Rect((0, 0, self.figure.get_width(), self.figure.get_height()))
        self.previous_rect = None

    def update_direction(self, direction):
        self.direction[0] += direction[0]
        self.direction[1] += direction[1]

    def update_position(self):
        x_offset = self.direction[0] * self.speed
        y_offset = self.direction[1] * self.speed
        # Normalise magnitude. Is necessary for hat input for diagonal movement.
        if abs(self.direction[0]) + abs(self.direction[1]) >= 2:
            x_offset /= math.sqrt(2)
            y_offset /= math.sqrt(2)

        self.previous_rect = self.current_rect.copy()
        self.current_rect.move_ip(x_offset, y_offset)

    def draw_figure_to_surface(self, surface, dirty_rects):
        self.update_position()
        pygame.draw.rect(surface, self.colour, self.previous_rect)  # Erase figure at old position
        surface.blit(self.figure, self.current_rect)  # Draw figure at new position

        dirty_rects.append(self.previous_rect)
        dirty_rects.append(self.current_rect)


def get_keyboard_direction(event):
    # Return x-direction, y-direction
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
    # Initialise second player if joystick connected
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    screen = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("mouse animation")
    font = pygame.font.SysFont("arial", 14)

    clock = pygame.time.Clock()

    # Program initialisation, first frame logic
    start_time = time.time()
    fps_rect = pygame.Rect((0, 0, 50, 16))
    player_1 = Player(RED, SPEED)
    if joystick:
        player_2 = Player(BLUE, SPEED)

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
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                key_direction = get_keyboard_direction(event)
                if key_direction:
                    if event.type == pygame.KEYDOWN:
                        direction = key_direction
                    else:
                        direction = -key_direction[0], -key_direction[1]
                    player_1.update_direction(direction)
            if joystick:
                if event.type == pygame.JOYHATMOTION:
                    if event.hat == 0:
                        player_2.direction = [event.value[0], -event.value[1]]
                elif event.type == pygame.JOYAXISMOTION:
                    if event.axis < 2:
                        player_2.direction[event.axis] = event.value

        # Draw players
        dirty_rects = [fps_rect]
        if joystick:
            player_2.draw_figure_to_surface(screen, dirty_rects)
        player_1.draw_figure_to_surface(screen, dirty_rects)

        # Draw FPS display
        pygame.draw.rect(screen, BLACK, fps_rect)
        text = font.render("FPS: " + str(current_fps), True, WHITE)
        screen.blit(text, (fps_rect.x, fps_rect.y))

        # Update display
        pygame.display.update(dirty_rects)  # Update only rects modified in this frame

        # Limit framerate
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    game()
