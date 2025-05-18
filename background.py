import pygame
pygame.init()

# game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 530
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# image loading
background_image = pygame.image.load('background.jpg')

# main function to display the background
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    game_window.blit(background_image, (0, 0))

    # update the display
    pygame.display.update()
pygame.quit()
