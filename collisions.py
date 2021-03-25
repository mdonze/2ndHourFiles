import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    # constructor - gets called when a new object is created
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
# will make a list to hold sprites
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# loop in python 
for i in range(50):
    # calling our Block constructor
    # makes a new Block, color black, size 20x15
    block = Block(BLACK, 20, 15)

    #Sets x and y to a random number
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # add the block to the lists
    block_list.add(block)
    all_sprites_list.add(block)

# creates a player Block
player = Block(RED, 20, 15)
# add the player block to the all sprites list
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()

# keeps track of collisions
score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # updates the score
    for block in blocks_hit_list:
        score += 1
        print(score)
    
    # Draws all the sprites in the group
    # calling blit() on all the sprites in the list
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
