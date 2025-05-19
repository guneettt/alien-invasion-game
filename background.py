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

# create a list to hold bullets
bullets = []
bullet_cooldown = 250
last_bullet_time = 0
ship_x = float(ship_rect.x)
# main function to display the background
running = True
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
    # draw 
    game_window.blit(background_image, (0, 0))
    game_window.blit(space_img, ship_rect)
    for bullet in bullets:
        bullet.draw(game_window)
    # update the display
    pygame.display.update()
pygame.quit()
