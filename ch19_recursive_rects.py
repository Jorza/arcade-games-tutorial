"""
 Recursively draw rectangles.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""
import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def recursive_draw(x, y, width, height):
    """ Recursive rectangle function. """
    pygame.draw.rect(screen, BLACK,
                     [x, y, width, height],
                     1)

    # Is the rectangle wide enough to draw again?
    if (width > 14):
        # Scale down
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        # Recursively draw again
        recursive_draw(x, y, width, height)


pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initial frame
screen.fill(WHITE)
recursive_draw(0, 0, 700, 500)
pygame.display.flip()

# -------- Main Program Loop -----------
# Loop until the user clicks the close button.
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
