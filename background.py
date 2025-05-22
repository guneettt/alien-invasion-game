import pygame
pygame.init()

# game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 530
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Alien Invasion Game")

# bg image loading
background_image = pygame.image.load('background.jpg')

# spaceship image loading
space_img = pygame.image.load('spaceship.png')
ship_rect = space_img.get_rect()

space_img = pygame.image.load('spaceship.png').convert_alpha()
space_img = pygame.transform.scale(space_img, (100, 100))  # scale down the image

ship_rect = space_img.get_rect()
ship_rect.midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 8)  # center horizontally, bottom margin

bullet_img = pygame.image.load('bullet.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (10, 20))  # scale down the image

# add the bullets 
class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 3

    def update(self):
        self.rect.y -= self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
# Alien class
alien_img = pygame.image.load('aliens.png').convert_alpha()
alien_img = pygame.transform.scale(alien_img, (60, 60))

class Alien:
    def __init__(self, x, y):
        self.image = alien_img
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Blast class
blast_img = pygame.image.load('blast.png').convert_alpha()
blast_img = pygame.transform.scale(blast_img, (60, 60))

class Blast:
    def __init__(self, x, y):
        self.image = blast_img
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = 15  # Show for 15 frames

    def update(self):
        self.timer -= 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# create a list to hold bullets
bullets = []
bullet_cooldown = 250
last_bullet_time = 0
ship_x = float(ship_rect.x)
# main function to display the background
running = True
# Create some aliens at the top
aliens = []
for i in range(5):  # 5 aliens across
    aliens.append(Alien(100 * i + 50, 50))

blasts = []  # store blast effects
# Create some aliens at the top
# Create a grid of aliens: 4 rows, 8 columns
aliens = []
rows = 4
cols = 9
alien_spacing_x = 80  # horizontal spacing
alien_spacing_y = 70  # vertical spacing
start_x = 60  # left margin
start_y = 40  # top margin

for row in range(rows):
    for col in range(cols):
        x = start_x + col * alien_spacing_x
        y = start_y + row * alien_spacing_y
        aliens.append(Alien(x, y))

blasts = []  # store blast effects

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_x -= 1
        if current_time - last_bullet_time > bullet_cooldown:
            bullets.append(Bullet(ship_rect.centerx, ship_rect.top)) # for shooting the bullets automatically
            last_bullet_time = current_time
    if keys[pygame.K_RIGHT]:
        ship_x += 1
        if current_time - last_bullet_time > bullet_cooldown:
            bullets.append(Bullet(ship_rect.centerx, ship_rect.top)) # for shooting the bullets automatically
            last_bullet_time = current_time
    ship_rect.x = int(ship_x)
    for bullet in bullets[:]:
        bullet.update()
        if bullet.rect.bottom < 0: #offscreen
            bullets.remove(bullet)
    # Check bullet-alien collisions
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.rect.colliderect(alien.rect):
                bullets.remove(bullet)
                aliens.remove(alien)
                blasts.append(Blast(alien.rect.centerx, alien.rect.centery))
                break

    # draw 
    game_window.blit(background_image, (0, 0))
    game_window.blit(space_img, ship_rect)
    for bullet in bullets:
        bullet.draw(game_window)
    # update the display
    # Draw aliens
    for alien in aliens:
        alien.draw(game_window)

    # Update and draw blasts
    for blast in blasts[:]:
        blast.update()
        blast.draw(game_window)
        if blast.timer <= 0:
            blasts.remove(blast)

    pygame.display.update()
pygame.quit()