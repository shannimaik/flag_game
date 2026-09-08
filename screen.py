# region-----------------------IMPORTS------------------------
import random
import pygame
import consts
from consts import WINDOW_WIDTH, WINDOW_HEIGHT, BUSH_WIDTH, BUSH_HEIGHT, \
    SOLDIER_WIDTH, SOLDIER_HEIGHT, FLAG_HEIGHT, FLAG_WIDTH, FLAG_COLS, \
    FLAG_ROWS, BOARD_ROWS, BOARD_COLS, CELL_SIZE

# endregion---------------------------------------------------


screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

''' create green game background'''
def open_screen():
        background_color = (consts.BACKGROUND_COLOR)
        pygame.display.set_caption('shanni and talya')
        screen.fill(background_color)
        print_random_grass()
        add_solider()
        add_flag()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


''' print 20 bushes  '''
def print_random_grass():
    img=pygame.image.load('grass.png')
    num_of_grass=20
    img = pygame.transform.scale(img, (BUSH_WIDTH, BUSH_HEIGHT))
    list_of_grass_locations = []
    for i in range(num_of_grass):
        x = random.randrange(1, WINDOW_WIDTH,BUSH_WIDTH)
        while x+60>WINDOW_WIDTH:
            x = random.randrange(1, WINDOW_WIDTH, BUSH_WIDTH)
        y = random.randrange(1, WINDOW_HEIGHT, BUSH_HEIGHT)
        while y + 40 > WINDOW_HEIGHT:
              y = random.randrange(1, WINDOW_HEIGHT,BUSH_HEIGHT)
        list_of_grass_locations.append((x,y))
        for pos in list_of_grass_locations:
            screen.blit(img,pos)




'''prints the solider a the top left corner'''
def add_solider():
    img = pygame.image.load('soldier.png')
    img = pygame.transform.scale(img, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
    screen.blit(img,(0,0))


'''prints the solider a the bottom right corner'''
def add_flag():
    img = pygame.image.load('flag.png')
    img = pygame.transform.scale(img, (FLAG_WIDTH ,FLAG_HEIGHT))
    screen.blit(img, ((BOARD_COLS-FLAG_COLS)*CELL_SIZE,(BOARD_ROWS-FLAG_ROWS)*CELL_SIZE))

open_screen()

