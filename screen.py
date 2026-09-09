
import random
import pygame
import consts

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, BUSH_HEIGHT, BUSH_WIDTH, GREEN, \
    CELL_SIZE, SOLDIER_ROWS, SOLDIER_COLS, FLAG_COLS, FLAG_ROWS, BOARD_ROWS, \
    BOARD_COLS, WHITE, BACKGROUND_COLOR, SOLDIER_WIDTH, SOLDIER_HEIGHT, \
    FLAG_WIDTH, FLAG_HEIGHT, MINE_HEIGHT, MINE_WIDTH


screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))
def open_screen(list_of_grass_locations, row, col ):
        background_color = (BACKGROUND_COLOR)
        pygame.display.set_caption('shanni and talya')
        screen.fill(background_color)
        print_random_grass(list_of_grass_locations)
        add_solider(row,col)
        add_flag()
        pygame.display.flip()

def get_grass_location():
    list_of_grass_locations = []
    for i in range(consts.BUSH_COUNT):
        x = random.randrange(1, WINDOW_WIDTH, BUSH_WIDTH)
        while x + BUSH_WIDTH > WINDOW_WIDTH:
            x = random.randrange(1, WINDOW_WIDTH, BUSH_WIDTH)
        y = random.randrange(1, WINDOW_HEIGHT, BUSH_HEIGHT)
        while y + BUSH_HEIGHT > WINDOW_HEIGHT:
            y = random.randrange(1, WINDOW_HEIGHT, BUSH_HEIGHT)
        list_of_grass_locations.append((x, y))
    return list_of_grass_locations

def print_random_grass(list_of_grass_locations):
    img=pygame.image.load('grass.png')
    img = pygame.transform.scale(img, (BUSH_WIDTH, BUSH_HEIGHT))
    for pos in list_of_grass_locations:
        screen.blit(img,pos)


'''prints the solider a the top left corner'''
def add_solider(row, col):
    img = pygame.image.load('soldier.png')
    img = pygame.transform.scale(img, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
    screen.blit(img,(col*CELL_SIZE,row*CELL_SIZE))


'''prints the solider a the bottom right corner'''
def add_flag():
    img = pygame.image.load('flag.png')
    img = pygame.transform.scale(img, (FLAG_WIDTH ,FLAG_HEIGHT))
    screen.blit(img, ((BOARD_COLS-FLAG_COLS)*CELL_SIZE,(BOARD_ROWS-FLAG_ROWS)*CELL_SIZE))


'''soldier in night mood'''

def add_green_solider():
        img = pygame.image.load('soldier_night.png')
        img = pygame.transform.scale(img, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
        screen.blit(img, (0, 0))


'''prints matrix'''
def print_matrix():
    screen.fill(consts.BLACK)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect, 1)
    add_green_solider()
    pygame.display.flip()


''' draw mines '''
def print_mines(mines_locations):
    img = pygame.image.load('mine.png')
    img = pygame.transform.scale(img, (MINE_WIDTH, MINE_HEIGHT))
    for pos in mines_locations:
        screen.blit(img,( pos[0]*CELL_SIZE,pos[1]*CELL_SIZE))



print_matrix()
def show_the_matrix_for_one_sec(list_of_grass_locations):
    print_matrix()
    pygame.display.flip()
    pygame.time.delay(1000)
    open_screen(list_of_grass_locations)
    pygame.display.flip()








'''print game message'''
def draw_game_message():
    draw_message(consts.GAME_MASSAGE_TEXT, consts.GAME_MASSAGE_FONT_SIZE,
                 consts.GAME_MASSAGE_COLOR, consts.GAME_MASSAGE_LOCATION)

''' print lose massage'''
def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

''' print win massage'''
def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


''' print massage'''
def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)