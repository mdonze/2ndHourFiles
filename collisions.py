import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

game_over = False
score = 0
class Block(pygame.sprite.Sprite):
    # constructor - gets called when a new object is created
    def __init__(self, width, height, imageFile):
        super().__init__()
        big_image = pygame.image.load(imageFile)
        # makes all the white transparent
        big_image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(big_image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-2, 2)
        self.y_vel = random.randrange(-2, 2)

    def change_x(self):
        self.x_vel = self.x_vel * -1

    def change_y(self):
        self.y_vel = self.y_vel * -1

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, fileName):
        super().__init__()
        big_ss = pygame.image.load(fileName)
        big_ss.set_colorkey([255, 255, 255])
        self.image = pygame.transform.scale(big_ss, (width, height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 350
        self.is_alive = True

    def update(self):
        pass

    def isDead(self):
        self.kill()
        self.is_alive = False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
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
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Score: " + str(score), True, RED, BLACK)
textRect = text.get_rect()
textRect.center = (100, 20) 

# loop in python 
for i in range(50):
    # calling our Block constructor
    # makes a new Block, color black, size 20x15
    block = Block(40, 40, "asteroid.png")

    #Sets x and y to a random number
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height - 200)

    # add the block to the lists
    block_list.add(block)
    all_sprites_list.add(block)

# creates a player Block
player = Player(30, 40, "spaceshipC.png")
# add the player block to the all sprites list
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()

# keeps track of collisions


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # event handler to make bullets
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet(RED, 4, 10)
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 20
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    if not game_over:
        screen.fill(BLACK)
        pos = pygame.mouse.get_pos()

        player.rect.x = pos[0]

        all_sprites_list.update()

        for bullet in bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # updates the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        
        for block in block_list:
            if pygame.sprite.collide_mask(block, player):
                player.isDead()
                game_over = True
            if block.rect.y > screen_height:
                block.change_y()
            if block.rect.y < 0:
                block.change_y()
            if block.rect.x > screen_width:
                block.rect.x = 0
            if block.rect.x < 0:
                block.rect.x = screen_width
        
        
        all_sprites_list.draw(screen)
        text = font.render("Score: " + str(score), True, RED, BLACK)
        screen.blit(text, textRect)
        
        # Draws all the sprites in the group
        # calling blit() on all the sprites in the list
    else:
        screen.fill(RED)
    
   

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
