"""
 Sample fractal using recursion.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


def recursive_draw(x, y, width, height, count):
    # Draw the rectangle
    # pygame.draw.rect(screen,black,[x,y,width,height],1)
    pygame.draw.line(screen,
                     black,
                     [x + width * .25, height // 2 + y],
                     [x + width * .75, height // 2 + y],
                     count * 2)
    pygame.draw.line(screen,
                     black,
                     [x + width * .25, (height * .5) // 2 + y],
                     [x + width * .25, (height * 1.5) // 2 + y],
                     count * 2)
    pygame.draw.line(screen,
                     black,
                     [x + width * .75, (height * .5) // 2 + y],
                     [x + width * .75, (height * 1.5) // 2 + y],
                     count * 2)

    if count > 0:
        count -= 1
        width = width // 2
        height = height // 2
        # Top left
        recursive_draw(x, y, width, height, count)
        # Top right
        recursive_draw(x + width, y, width, height, count)
        # Bottom left
        recursive_draw(x, y + height, width, height, count)
        # Bottom right
        recursive_draw(x + width, y + height, width, height, count)


pygame.init()

# Set the height and width of the screen
size = [700, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initial frame
fractal_level = 6

screen.fill(white)
recursive_draw(0, 0, 700, 700, fractal_level)
pygame.display.flip()

# -------- Main Program Loop -----------
# Loop until the user clicks the close button.
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Limit to 20 frames per second
    clock.tick(20)

pygame.quit()
