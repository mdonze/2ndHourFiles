import pygame

# This line must be in all pygames
pygame.init()
# variable to hold the screen size
size = [700, 500]
# variable to hold a reference to the screen
screen = pygame.display.set_mode(size)
# variable to control the game loop
playing = True
# variable is used to control 
# how fast the screen updates
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# Colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)
    # Legs
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 2)
    # Body
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)
    # Arms
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)

# Game Loop
while playing:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        # User let up on a key
        elif event.type == pygame.KEYUP:
             # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    
    # Game logic goes here
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    # Drawing goes here
    screen.fill(WHITE)
    draw_stick_figure(screen, x_coord, y_coord)

    # This must be at the end of the drawing
    pygame.display.flip()

    # Set the fps to 60
    clock.tick(60)