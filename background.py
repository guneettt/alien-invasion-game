import pygame
pygame.init()

# game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 530
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# bg image loading
background_image = pygame.image.load('background.jpg')

# spaceship image loading
space_img = pygame.image.load('spaceship.png')
ship_rect = space_img.get_rect()
ship_rect.center = (WINDOW_WIDTH // 200, WINDOW_HEIGHT // 200)
space_img = pygame.image.load('spaceship.png').convert_alpha()
space_img = pygame.transform.scale(space_img, (100, 100))  # scale down the image

ship_rect = space_img.get_rect()
ship_rect.midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 8)  # center horizontally, bottom margin


# main function to display the background
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= 1
    if keys[pygame.K_RIGHT]:
        ship_rect.x += 1

    # draw the background
    game_window.blit(background_image, (0, 0))
    # draw the spaceship
    game_window.blit(space_img, ship_rect)

    # update the display
    pygame.display.update()
pygame.quit()
