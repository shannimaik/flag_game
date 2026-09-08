import pygame
from Tools.scripts.dutree import show
WINDOW_WIDTH=50*20
WINDOW_HEIGHT=25*20
BACKGROUND_COLOR = (138, 201, 38)

screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))
def open_screen():
        background_color = (BACKGROUND_COLOR)
        pygame.display.set_caption('shanni and talya')
        screen.fill(background_color)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
