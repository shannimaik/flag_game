# region-----------------------IMPORTS------------------------
import random
import pygame
import consts
from consts import WINDOW_WIDTH, WINDOW_HEIGHT,BUSH_WIDTH, BUSH_HEIGHT
# endregion---------------------------------------------------


screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

''' create green game background'''
def open_screen():
        background_color = (consts.BACKGROUND_COLOR)
        pygame.display.set_caption('shanni and talya')
        screen.fill(background_color)
        print_random_grass()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


''' PRINTS 20 GRASSESS  '''
def print_random_grass():
    img=pygame.image.load('grass.png')
    num_of_grass=20
    img = pygame.transform.scale(img, (BUSH_WIDTH, BUSH_HEIGHT))
    running = True
    list_of_grass_locations = []
    for i in range(num_of_grass):
        x = random.randrange(1, WINDOW_WIDTH,BUSH_WIDTH)
        while x+60>WINDOW_WIDTH:
            x = random.randrange(1, WINDOW_WIDTH, BUSH_WIDTH)
        y = random.randrange(1, WINDOW_HEIGHT, BUSH_HEIGHT)
        while y + 40 > WINDOW_HEIGHT:
              y = random.randrange(1, WINDOW_HEIGHT,BUSH_HEIGHT)
        list_of_grass_locations.append((x,y))
    while running:
        for pos in list_of_grass_locations:
            screen.blit(img,pos)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

open_screen()

