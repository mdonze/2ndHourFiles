import pygame
import random

#TODO Make Blocks move randomly - Done
#TODO Replace blocks with pictures - Done
#TODO make the player shoot (next class)
#TODO Make seperate classes for the spaceship and bullets
#TODO Replace horrible sprites with decent sprites

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    # constructor - gets called when a new object is created
    def __init__(self, color, width, height, imageFile):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-2, 2)
        self.y_vel = random.randrange(-2, 2)

    def moveBlock(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

class Player(pygame.sprite.Sprite):
    def __init__(self, fileName):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image = pygame.image.load(fileName)
        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3



pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
# will make a list to hold sprites
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
# list to hold our bullets
bullet_list = pygame.sprite.Group()

# loop in python 
for i in range(50):
    # calling our Block constructor
    # makes a new Block, color black, size 20x15
    block = Block(BLACK, 20, 15, "rock2.png")

    #Sets x and y to a random number
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # add the block to the lists
    block_list.add(block)
    all_sprites_list.add(block)

# creates a player Block
player = Player("spaceship.png")
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
        # event handler to make bullets
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

    # updates the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
    
    for block in block_list:
        block.moveBlock()
    
    for bullet in bullet_list:
        bullet.update()

    
    
    # Draws all the sprites in the group
    # calling blit() on all the sprites in the list
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
