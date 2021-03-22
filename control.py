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

# draw stick_figure
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

RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Game Loop
while playing:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    # Game logic goes here
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # Drawing goes here
    screen.fill(WHITE)
    draw_stick_figure(screen, x, y)

    # This must be at the end of the drawing
    pygame.display.flip()

    # Set the fps to 60
    clock.tick(60)